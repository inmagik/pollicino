from django.contrib import admin

from .models import App, ClientToken

class AppAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class ClientTokenAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(App, AppAdmin)
admin.site.register(ClientToken, ClientTokenAdmin)