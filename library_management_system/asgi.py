import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from users import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management_system.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/some_path/", consumers.SomeConsumer.as_asgi()),
        ])
    ),
})