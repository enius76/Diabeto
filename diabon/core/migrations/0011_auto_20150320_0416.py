# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150320_0353'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category_article',
            new_name='Categoryarticle',
        ),
    ]
