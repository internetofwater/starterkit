# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StringSettings',
            fields=[
                ('value', models.TextField(blank=True)),
                ('identifier', models.TextField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'string_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UriSettings',
            fields=[
                ('value', models.TextField(blank=True)),
                ('identifier', models.TextField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'uri_settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ediml', models.TextField(blank=True, null=True)),
                ('sensorml', models.TextField(blank=True, null=True)),
                ('fileid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'permissions': (('admin_sos', 'Can admin SOS'), ('read_sos', 'Can retrieve data from SOS')),
            },
        ),
    ]