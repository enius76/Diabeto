# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20150324_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 3, 13, 35, 494000)),
            preserve_default=True,
        ),
    ]
