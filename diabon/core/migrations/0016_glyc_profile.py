# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_auto_20150323_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glyc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user', models.IntegerField(default=0)),
                ('value', models.FloatField()),
                ('time', models.DateTimeField(default=datetime.datetime(2015, 3, 23, 16, 58, 58, 695000))),
                ('note', models.CharField(default=b' ', max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth', models.DateField(default=datetime.datetime(2015, 3, 23, 16, 58, 58, 695000))),
                ('sexe', models.CharField(max_length=1)),
                ('weight', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('glyc', models.ForeignKey(to='core.Glyc')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
