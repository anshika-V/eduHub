from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from .modelsOperation import TestModelModifier


class TestMaker(JsonWebsocketConsumer):
    Modifier = None

    def connect(self):
        usr = self.scope['user']
        if (not usr.is_authenticated):
            self.close()
            return
        elif (usr.profile.type == 'S'):
            self.close()
            return
        self.Modifier = TestModelModifier(user=usr)
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        print(content)
        response = self.Modifier.action(content['type'], content['payload'])
        print(response)
        if response == None:
            response = {'type': 'None'}
        self.send_json(response)