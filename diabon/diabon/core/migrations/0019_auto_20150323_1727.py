# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_glyc_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='glyc',
        ),
        migrations.AlterField(
            model_name='glyc',
            name='id_user',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 17, 27, 7, 157000)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 17, 27, 7, 157000)),
            preserve_default=True,
        ),
    ]
