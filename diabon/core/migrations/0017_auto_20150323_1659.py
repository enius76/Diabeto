# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_glyc_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='glyc',
        ),
        migrations.DeleteModel(
            name='Glyc',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
