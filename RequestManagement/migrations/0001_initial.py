# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AccountManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
                ('listen_account', models.ForeignKey(related_name='listen_user', to='AccountManagement.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField(null=True)),
                ('category', models.CharField(default=b'General', max_length=50)),
                ('price', models.CharField(max_length=50, null=True)),
                ('price_currency', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(default=1, max_length=50)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 11, 8, 21, 52, 48, 642000))),
                ('closed_date', models.DateTimeField(null=True)),
                ('expired_date', models.DateTimeField(null=True)),
                ('asap', models.BooleanField(default=True)),
                ('last_modified_date', models.DateTimeField(null=True)),
                ('origin_city', models.CharField(max_length=225)),
                ('origin_address', models.TextField(null=True)),
                ('destination_city', models.CharField(max_length=225)),
                ('destination_address', models.TextField(null=True)),
                ('view_num', models.IntegerField(default=0)),
                ('image_url', models.TextField(null=True)),
                ('thumb_url', models.TextField(null=True)),
                ('account', models.ForeignKey(to='AccountManagement.Account')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='request',
            field=models.ForeignKey(to='RequestManagement.Request'),
        ),
        migrations.AddField(
            model_name='chat',
            name='speak_account',
            field=models.ForeignKey(related_name='speak_user', to='AccountManagement.Account'),
        ),
    ]
