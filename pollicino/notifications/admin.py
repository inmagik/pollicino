from django.contrib import admin

from .models import PushConfiguration, Installation, NotificationMessage, DeviceFeedBack

admin.site.register(PushConfiguration)
admin.site.register(Installation)
admin.site.register(NotificationMessage)
admin.site.register(DeviceFeedBack)



