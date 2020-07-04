from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from .modelsOperation import TestModelModifier
from material.models import Test
from datetime import datetime
from django.core import serializers
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

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        print(content)
        pass
