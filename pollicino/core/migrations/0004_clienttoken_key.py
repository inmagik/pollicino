# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160209_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienttoken',
            name='key',
            field=models.CharField(default='3', editable=False, max_length=100),
            preserve_default=False,
        ),
    ]
