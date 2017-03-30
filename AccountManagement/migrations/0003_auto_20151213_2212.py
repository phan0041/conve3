# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('AccountManagement', '0002_auto_20151207_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 13, 22, 12, 59, 465000)),
        ),
    ]
