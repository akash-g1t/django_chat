from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import EchoConsumer, ChatConsumer
from channels.auth import AuthMiddlewareStack
from chat.token_authentication_stack import TokenAuthMiddleware
from django.core.asgi import get_asgi_application 

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/chat/<str:username>/', ChatConsumer.as_asgi()),
                path('ws/chat/', EchoConsumer.as_asgi())
            ])
        )
    )
})