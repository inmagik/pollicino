# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20160209_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='device_token',
            field=models.CharField(max_length=200),
        ),
    ]
