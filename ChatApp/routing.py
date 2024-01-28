from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import WaveSync.routing


application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            WaveSync.routing.websocket_urlpatterns
        )
    )
})



