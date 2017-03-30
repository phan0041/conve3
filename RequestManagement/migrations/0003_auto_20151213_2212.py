# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('RequestManagement', '0002_auto_20151213_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 13, 22, 12, 59, 465000)),
        ),
    ]
