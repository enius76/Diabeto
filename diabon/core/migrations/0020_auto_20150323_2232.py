# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150323_1727'),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 22, 32, 40, 954000)),
            preserve_default=True,
        ),
    ]
