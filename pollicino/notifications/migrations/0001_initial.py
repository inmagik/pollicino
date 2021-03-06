# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 12:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceFeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_token', models.CharField(max_length=200)),
                ('fail_time', models.DateTimeField()),
                ('use_sandbox', models.BooleanField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.App')),
            ],
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_token', models.CharField(max_length=200, unique=True)),
                ('registration_id', models.CharField(max_length=200, unique=True)),
                ('platform', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('app_version', models.CharField(max_length=200)),
                ('locale', models.CharField(blank=True, max_length=200, null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.App')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.IntegerField(blank=True, default=0, null=True)),
                ('sound', models.CharField(blank=True, default='default', max_length=200, null=True)),
                ('alert', models.TextField()),
                ('send', models.BooleanField()),
                ('sent', models.BooleanField(editable=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.App')),
            ],
        ),
        migrations.CreateModel(
            name='PushConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apns_certificate', models.FileField(null=True, upload_to='apns_certificates')),
                ('apns_certificate_dev', models.FileField(null=True, upload_to='apns_certificates_dev')),
                ('gcm_api_key', models.CharField(blank=True, max_length=200, null=True)),
                ('use_sandbox', models.BooleanField(default=True)),
                ('gcm_max_recipients', models.PositiveSmallIntegerField(default=1000, validators=[django.core.validators.MaxValueValidator(1000)])),
                ('app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.App')),
            ],
        ),
    ]
