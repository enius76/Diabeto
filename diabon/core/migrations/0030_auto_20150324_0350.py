# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20150324_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 24, 3, 50, 1, 324000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 24, 3, 50, 1, 324000)),
            preserve_default=True,
        ),
    ]
