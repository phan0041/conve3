# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AccountManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='thumb_link',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 7, 23, 1, 32, 281000)),
        ),
    ]
