from django.contrib import admin

from .models import App, ClientToken

admin.site.register(App)
admin.site.register(ClientToken)