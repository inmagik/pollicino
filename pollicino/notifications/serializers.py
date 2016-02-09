from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
#from core.models import App

class SimpleInstallationSerializer(serializers.Serializer):
    device_token = serializers.CharField()
    platform = serializers.CharField()
    app_version = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        device_token = attrs.get('device_token')
        platform = attrs.get('platform')

        if device_token and platform:
            pass
        else:
            msg = _('Must include "platform" and "device_token".')
            raise serializers.ValidationError(msg)

        return attrs