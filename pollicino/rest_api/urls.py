from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from core.views import obtain_client_auth
from notifications.views import register_device_view

#router = SimpleRouter()


urlpatterns = [
    url(r'^auth-client/', obtain_client_auth, name="auth-client"),
    url(r'^register-installation/', register_device_view, name="register-installation"),
]

