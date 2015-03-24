# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150323_1727'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Glyc',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 20, 6, 59, 124000)),
            preserve_default=True,
        ),
    ]
