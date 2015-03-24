# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20150323_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 22, 46, 17, 457000)),
            preserve_default=True,
        ),
    ]
