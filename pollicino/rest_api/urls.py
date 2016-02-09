from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from core.views import obtain_client_auth

#router = SimpleRouter()


urlpatterns = [
    url(r'^auth-client/', obtain_client_auth, name="auth-client"),
]

