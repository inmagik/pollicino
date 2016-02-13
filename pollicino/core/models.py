from __future__ import unicode_literals

import uuid
from django.db import models
from .utils import generate_jwt

def getuuid():
    return str(uuid.uuid4())

class App(models.Model):
    """
    Client app model.
    All models will be related to this one.
    """
    id = models.CharField(primary_key=True, default=getuuid, editable=False, max_length=200)
    name = models.CharField(max_length=255)
    # for now we keep a single client secret.
    # probably will be moved to a separate table
    client_secret = models.UUIDField(default=uuid.uuid4)



    def __unicode__(self):
        return self.name


class ClientToken(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    app = models.ForeignKey(App, null=True)
    key = models.CharField(max_length=100, editable=False)
    client_secret = models.UUIDField(unique=True)

    def save(self, *args, **kwargs):
        self.key = generate_jwt({"client_secret":self.client_secret, "app_id":self.app.id})
        return super(ClientToken, self).save(*args, **kwargs)
