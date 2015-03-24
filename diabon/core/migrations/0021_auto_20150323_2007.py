# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150323_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glyc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user', models.IntegerField()),
                ('value', models.FloatField()),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 3, 23, 20, 7, 49, 660000))),
                ('note', models.CharField(default=b' ', max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 3, 23, 20, 7, 49, 660000)),
            preserve_default=True,
        ),
    ]
