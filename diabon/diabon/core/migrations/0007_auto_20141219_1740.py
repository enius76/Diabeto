# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20141219_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='picture',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(max_length=200),
            preserve_default=True,
        ),
    ]
