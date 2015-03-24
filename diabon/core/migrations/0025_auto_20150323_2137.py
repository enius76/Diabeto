# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20150323_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glyc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user', models.IntegerField()),
                ('value', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=5)),
                ('note', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 21, 37, 4, 436000)),
            preserve_default=True,
        ),
    ]
