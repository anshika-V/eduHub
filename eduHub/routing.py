from channels.routing import ProtocolTypeRouter, URLRouter
from material.api.ws.rouing import websocket_urlpatterns as materials_ws_urls
from channels.auth import AuthMiddlewareStack
from django.urls import path

#Entry point for the whole ASGI APP
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(  #Author middleware stack for authentication
        URLRouter(
            materials_ws_urls  # deals with all asgi/web socket request related to materials app
        )
    ),
})
