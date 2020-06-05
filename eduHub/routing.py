from channels.routing import ProtocolTypeRouter, URLRouter
from material.api.ws.rouing import websocket_urlpatterns as materials_ws_urls
# from channels.staticfiles import StaticFilesConsumer
from channels.auth import AuthMiddlewareStack
from django.urls import path

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    # 'http.request': StaticFilesConsumer(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            materials_ws_urls
        )
    ),
})
