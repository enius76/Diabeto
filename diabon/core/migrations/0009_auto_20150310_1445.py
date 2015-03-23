# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150309_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='glucide',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
