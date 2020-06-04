from channels.routing import URLRouter
from django.urls import re_path, path, include
from . import consumers

urlpatterns = [
    path('testMaker/',consumers.TestMaker),
]

websocket_urlpatterns = [
    path('ws/material/', URLRouter(urlpatterns))
]

