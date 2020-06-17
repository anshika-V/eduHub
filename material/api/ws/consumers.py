from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from .modelsOperation import TestModelModifier

# WS consumer for Create test


class TestMaker(JsonWebsocketConsumer):
    Modifier = None

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
