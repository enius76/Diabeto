# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20150323_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glyc',
            name='date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 22, 35, 28, 155000)),
            preserve_default=True,
        ),
    ]
