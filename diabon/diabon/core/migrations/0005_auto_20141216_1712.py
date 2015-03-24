# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_glyc_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glyc',
            name='time',
        ),
        migrations.AlterField(
            model_name='glyc',
            name='value',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
