# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141216_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=b' ', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food',
            name='slug',
            field=models.SlugField(default=b' ', max_length=200),
            preserve_default=True,
        ),
    ]
