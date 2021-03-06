# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clienttoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clienttoken',
            old_name='key',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='app',
            name='client_secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
