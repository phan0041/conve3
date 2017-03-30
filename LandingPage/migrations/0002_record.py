# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=50)),
                ('shipper_name', models.CharField(max_length=50)),
                ('kg_available', models.CharField(default=b'None', max_length=200, null=True)),
                ('date', models.DateField(null=True)),
                ('price', models.CharField(default=b'None', max_length=200, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('pick_up_destination', models.CharField(default=b'None', max_length=100, null=True)),
                ('release_destination', models.CharField(default=b'None', max_length=100, null=True)),
                ('note', models.CharField(max_length=1000, null=True)),
                ('url', models.TextField(max_length=500, null=True, validators=[django.core.validators.URLValidator()])),
                ('code', models.CharField(default=b'None', max_length=50, unique=True, null=True)),
                ('is_checked', models.BooleanField(default=False)),
            ],
        ),
    ]
