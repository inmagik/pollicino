# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientToken',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_secret', models.UUIDField(unique=True)),
            ],
        ),
    ]
