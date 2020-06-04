from channels.routing import ProtocolTypeRouter, URLRouter
from material.api.ws.rouing import websocket_urlpatterns as materials_ws_urls
from channels.auth import AuthMiddlewareStack
from django.urls import path

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)

    'websocket': AuthMiddlewareStack(
        URLRouter(
            materials_ws_urls
        )
    ),
})
