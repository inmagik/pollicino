from __future__ import unicode_literals

import uuid
from django.db import models


class App(models.Model):
    """
    Client app model.
    All models will be related to this one.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    # for now we keep a single client secret.
    # probably will be moved to a separate table
    client_secret = models.UUIDField(default=uuid.uuid4, editable=False)



    def __str__(self):
        return self.name

