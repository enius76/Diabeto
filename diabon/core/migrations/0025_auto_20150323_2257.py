# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20150323_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 22, 57, 10, 608000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 22, 57, 10, 608000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='glycMoyenne',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
