# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0023_auto_20150323_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birth', models.DateField(default=datetime.datetime(2015, 3, 23, 22, 47, 1, 72000))),
                ('sexe', models.CharField(max_length=1)),
                ('weight', models.FloatField(default=0.0)),
                ('height', models.FloatField(default=0.0)),
                ('picture', models.ImageField(upload_to=b'')),
                ('typeDiabete', models.CharField(max_length=50)),
                ('glycMoyenne', models.IntegerField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='glyc',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 23, 22, 47, 1, 72000)),
            preserve_default=True,
        ),
    ]
