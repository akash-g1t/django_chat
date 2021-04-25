"""
ASGI config for chat_demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_demo.settings')

application = get_asgi_application()

# If you want to put ASGI_APPLICATION via this file than comment above 'application' line and 
# uncomment below lines:

# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import path
# from chat.consumers import EchoConsumer, ChatConsumer
# from channels.auth import AuthMiddlewareStack
# from chat.token_authentication_stack import TokenAuthMiddleware
# from django.core.asgi import get_asgi_application 

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': TokenAuthMiddleware(
#         AuthMiddlewareStack(
#             URLRouter([
#                 path('ws/chat/<str:username>/', ChatConsumer.as_asgi()),
#                 path('ws/chat/', EchoConsumer.as_asgi())
#             ])
#         )
#     )
# })