from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from .modelsOperation import TestModelModifier
from mymodule.wsClient import JsonAsyncClient
from material.models import Test, TestResult
from django.core import serializers
from datetime import datetime
import json
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
class StudentTest(JsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.test = None  # model.test object, the test user is taking
        # model.TestResult object, the test result where the response of users test is saving
        self.test_result = None
        self.test_response_data = None  # parsed json data of test_result.question

    def connect(self):  # Add websocket securities later
        self.user = self.scope['user']
        if (not self.user.is_authenticated):  # implementation of @login_required
            self.close()
            return
        test = None
        try:
            test = Test.objects.get(
                pk=self.scope['url_route']['kwargs']['test'])
        except:
            self.close()
            return
        self.test = test  # registering test to the class instance variable
        testResults = self.user.testresult_set.all().filter(parent_test=test)
        attempted = testResults.exists()
        if (attempted):  # if already attempted return the page showing laready attempted
            if (test.duration != -1):
                # timedalta difference of curenttime and time of test response
                time_lapse = datetime.utcnow() - testResults.first().time.replace(tzinfo=None)
                time_lapse_seconds = int(time_lapse.total_seconds())
                # if more than the specified duration of test.duration has passed since test response object have been saved ot sice the student started the test
                if (time_lapse_seconds > test.duration * 60):
                    self.close()
                    return
                else:  # reconnecting
                    self.accept()
                    self.test_result = testResults.first()
                    self.test_response_data = json.loads(
                        self.test_result.questions)
                    json_test_data = serializers.serialize(
                        'json', [test], use_natural_foreign_keys=True)
                    json_test_data = json.loads(json_test_data)[0]
                    json_test_data['questions'] = self.test_response_data
                    json_test_data['startTime'] = str(self.test_result.time)
                    res = {'type': 'reconnected',
                           'TestData': json_test_data}
                    # sending test result data if reconnecting
                    self.send_json(res)
                    return
            else:
                self.close()
                return
        self.accept()  # Accepting the connection and then sending all the test data
        json_test_data = serializers.serialize(
            'json', [test],  use_natural_foreign_keys=True)
        json_test_data = json.loads(json_test_data)[0]
        questions = test.question_set.all()
        question_data = serializers.serialize('json', questions)
        question_data = json.loads(question_data)
        # Adding all theh questions of the test in the response
        json_test_data['questions'] = question_data
        res = {'type': 'connected', 'TestData': json_test_data}
        self.send_json(res)  # sending test data
        # storing test question data as it was sent to the react app for further saving it to Test Response
        self.test_response_data = question_data

    def disconnect(self, close_code):
        if (self.test_result):
            self.test_result.questions = json.dumps(self.test_response_data)
            self.test_result.save()

    def enterTest(self):
        res = {'type': 'data_received'}
        if(self.test_result == None):
            data = None
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
            self.test_result.save()
        else:
            pass
        self.send_json(res)

    def questionUpdate(self, data, index):
        self.test_response_data[index].update(data)
        self.send_json({'type': 'question_received'})

    def submit(self, marks):
        i = 0
        for question in self.test_response_data:
            question.update({'marks': marks[i]})
            i = i + 1
        self.test_result.questions = json.dumps(self.test_response_data)
        self.test_result.save()
        res = {'type': 'submitted'}
        self.send_json(res)

    def receive_json(self, content):
        try:
            if (content['type'] == 'questionUpdate'):
                self.questionUpdate(content['payload'], content['index'])
            elif (content['type'] == 'enter'):
                self.enterTest()
            elif (content['type'] == 'submit'):
                self.submit(content['marks'])
        except:
            pass


class FerSocket(JsonAsyncClient):  # ws client module to connect to fer dedicated server

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ws = 'ws://fer.southeastasia.cloudapp.azure.com/'

    def received_json():
        pass
