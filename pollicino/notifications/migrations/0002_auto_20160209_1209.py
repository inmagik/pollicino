# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationmessage',
            name='sent',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
