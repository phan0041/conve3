# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RequestManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('username', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField()),
                ('request_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='chat',
            name='listen_account',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='request',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='speak_account',
        ),
        migrations.AlterField(
            model_name='request',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 13, 22, 11, 31, 718000)),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
