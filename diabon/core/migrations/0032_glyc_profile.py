# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0031_auto_20150324_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glyc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_user', models.IntegerField()),
                ('value', models.FloatField()),
                ('date', models.DateTimeField()),
                ('time', models.CharField(max_length=5)),
                ('note', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth', models.DateField(default=datetime.datetime(2015, 3, 24, 5, 26, 44, 606000))),
                ('sexe', models.CharField(max_length=1)),
                ('weight', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('typeDiabete', models.CharField(max_length=50)),
                ('glycMoyenne', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
