# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150323_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glyc',
            name='note',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 20, 17, 36, 219000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 20, 17, 36, 219000)),
            preserve_default=True,
        ),
    ]
