from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from .models import App

class ClientTokenSerializer(serializers.Serializer):
    app_id = serializers.CharField()
    client_secret = serializers.CharField()

    def validate(self, attrs):
        app_id = attrs.get('app_id')
        client_secret = attrs.get('client_secret')

        if app_id and client_secret:

            try:
                app = App.objects.get(pk=app_id, client_secret=client_secret)

            except App.DoesNotExist:
                msg = _('Wrong client credentials')
                raise serializers.ValidationError(msg)
            except Exception, e:
                msg = _('Wrong client credentials')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "app_id" and "client_secret".')
            raise serializers.ValidationError(msg)

        return attrs