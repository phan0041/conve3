# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 11, 8, 21, 52, 48, 635000))),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('extra_phone', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('photo_link', models.TextField(null=True)),
                ('facebook_link', models.URLField(null=True)),
                ('view_num', models.IntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('user', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
