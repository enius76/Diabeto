# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20150323_2019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Glyc',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 21, 35, 40, 360000)),
            preserve_default=True,
        ),
    ]
