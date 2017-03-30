# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conve_facebook_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='SocialProfile',
        ),
    ]
