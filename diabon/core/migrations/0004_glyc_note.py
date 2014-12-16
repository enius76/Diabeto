# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_glyc_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='glyc',
            name='note',
            field=models.CharField(default=b' ', max_length=150),
            preserve_default=True,
        ),
    ]
