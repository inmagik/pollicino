# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_clienttoken_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienttoken',
            name='app',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.App'),
        ),
    ]