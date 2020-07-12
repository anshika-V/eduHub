from django.core.files.storage import default_storage as storage
from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from .AsyncDatabase import AsyncDatabase, AsyncDatabaseStudentTest
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from .modelsOperation import TestModelModifier
from mymodule.wsClient import JsonAsyncClient
from material.models import Test, TestResult
from django.core import serializers
from datetime import datetime
import json
import io
# WS consumer for Create test


class TestMaker(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Modifier = None

    def connect(self):
        usr = self.scope['user']
        if (not usr.is_authenticated):
            self.close()
            return
        elif (usr.profile.type != 'I'):
            self.close()
            return
        # initilizing the TestModelModifier class
        self.Modifier = TestModelModifier(user=usr)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        # Sending content to TesrModifier class for action
        response = self.Modifier.action(content['type'], content['payload'])
        if response == None:
            response = {'type': 'None'}
        self.send_json(response)


# Make this socket secure it probably not secure at the moment
class StudentTest(AsyncJsonWebsocketConsumer, AsyncDatabaseStudentTest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.test = None  # model.test object, the test user is taking
        # model.TestResult object, the test result where the response of users test is saving
        self.test_result = None
        self.test_response_data = None  # parsed json data of test_result.question
        self.fer_path = None  # path in the container where the image for fer is stored
        self.fer = None

    async def connect(self):  # Add websocket securities later
        self.user = self.scope['user']
        if (not self.user.is_authenticated):  # implementation of @login_required
            await self.close()
            return
        test = None
        try:
            test = await self.getTestFromPk(
                self.scope['url_route']['kwargs']['test'])
        except:
            await self.close()
            return
        self.test = test  # registering test to the class instance variable
        self.fer_path = 'analyser/' + self.user.username + '/' + test.title + '/'
        attempted = await self.getTestResultsOfUser()
        if (attempted):  # if already attempted return the page showing laready attempted
            if (test.duration != -1):
                # timedalta difference of curenttime and time of test response
                time_lapse = datetime.utcnow() - self.test_result.time.replace(tzinfo=None)
                time_lapse_seconds = int(time_lapse.total_seconds())
                # if more than the specified duration of test.duration has passed since test response object have been saved ot sice the student started the test
                if (time_lapse_seconds > test.duration * 60):
                    await self.close()
                    return
                else:  # reconnecting
                    await self.accept()
                    self.test_response_data = json.loads(
                        self.test_result.questions)
                    json_test_data = await self.serializeTest()
                    json_test_data = json.loads(json_test_data)[0]
                    json_test_data['questions'] = self.test_response_data
                    json_test_data['startTime'] = str(self.test_result.time)
                    res = {'type': 'reconnected',
                           'TestData': json_test_data}
                    # sending test result data if reconnecting
                    await self.send_json(res)
                    return
            else:
                await self.close()
                return
        await self.accept()  # Accepting the connection and then sending all the test data
        json_test_data = await self.serializeTest()
        json_test_data = json.loads(json_test_data)[0]
        question_data = await self.serialisedQuestionsOfTest()
        question_data = json.loads(question_data)
        # Adding all theh questions of the test in the response
        json_test_data['questions'] = question_data
        res = {'type': 'connected', 'TestData': json_test_data}
        await self.send_json(res)  # sending test data
        # storing test question data as it was sent to the react app for further saving it to Test Response
        self.test_response_data = question_data

    async def disconnect(self, close_code):
        if (self.test_result):
            self.test_result.questions = json.dumps(self.test_response_data)
            await self.saveModelObject(self.test_result)

    async def enterTest(self):
        res = {'type': 'data_received'}
        if(self.test_result == None):
            data = None
            # self.test_response_data is already initilized in connect method
            questions = self.test_response_data
            # subroutine to add answer and marks field to the question as done in the frontend react app

            def addFields(question):
                ans = ''
                if (question['fields']['type'] in ['O', 'M', 'ON', 'MP', 'MN', 'MPN']):
                    ans = [0, 0, 0, 0]
                question.update(
                    {'answer': ans, 'state': [0, 0, 0]})
                return question
            data = list(map(addFields, questions))
            self.test_response_data = data
            data = json.dumps(data)
            self.test_result = TestResult(
                student=self.user, parent_test=self.test, questions=data)
            await self.saveModelObject(self.test_result)
        else:
            pass
        await self.send_json(res)

    async def questionUpdate(self, data, index):
        self.test_response_data[index].update(data)
        await self.send_json({'type': 'question_received'})

    async def submit(self, marks):
        i = 0
        for question in self.test_response_data:
            question.update({'marks': marks[i]})
            i = i + 1
        self.test_result.questions = json.dumps(self.test_response_data)
        await self.saveModelObject(self.test_result)
        res = {'type': 'submitted'}
        await self.send_json(res)
        if (self.fer):
            self.fer.test_result = self.test_result
            await self.fer.send_json({'type': 'noData'})

    async def fer_image_save(self, payload):
        image_data = io.BytesIO(bytearray(payload['image']))
        file_name = storage.save(self.fer_path + payload['name'], image_data)
        res = {'type': 'data_received'}
        await self.send_json(res)
        msg = {
            'type': 'analyze',
            'payload': {
                'image': payload['name'],
                'question_number': payload['question_number']
            }
        }
        await self.fer.send_json(msg)

    async def initilizeFER(self):
        self.fer = FerSocket(path=self.fer_path)
        await self.fer.connect()
        await self.fer.send_json({'type': 'new', 'path': self.fer_path})
        res = {'type': 'fer_ready'}
        await self.send_json(res)

    async def closeFER(self):
        await self.fer.send_json({'type': 'close'})
        await self.fer.disconnect()
        self.fer = None  # test if the reference of class object is deleted or is still alive
        res = {'type': 'data_received'}
        await self.send_json(res)

    async def receive_json(self, content):
        try:
            if (content['type'] == 'ferimage'):
                print('fer_image received name = ')
                print(content['payload']['name'])
                await self.fer_image_save(content['payload'])
            elif (content['type'] == 'questionUpdate'):
                print(content)
                await self.questionUpdate(content['payload'], content['index'])
            elif (content['type'] == 'enter'):
                print(content)
                await self.enterTest()
            elif (content['type'] == 'submit'):
                print(content)
                await self.submit(content['marks'])
            elif (content['type'] == 'initilizeFER'):
                print(content)
                await self.initilizeFER()
            elif (content['type'] == 'closeFER'):
                print(content)
                await self.closeFER()
        except:
            pass


# ws client module to connect to fer dedicated server
class FerSocket(JsonAsyncClient, AsyncDatabase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uri = 'ws://fer.southeastasia.cloudapp.azure.com/ws/analyser/'
        self.id = None
        self.path = None
        self.test_result = None
        self.__dict__.update(kwargs)

    async def received_json(self, data):
        print('received from fer')
        print(data)
        try:
            if (data['code'] == 'new'):
                self.id = data['id']
            elif (data['code'] == 'closed'):
                await self.disconnect()
            elif (data['code'] == 'result'):
                self.test_result.fer_data = json.dumps(data['result'])
                await self.saveModelObject(self.test_result)
                await self.send_json({'type': 'close'})
                await self.disconnect()

        except:
            pass
