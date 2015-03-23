# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to=b'static/upload/')),
                ('weight', models.IntegerField()),
                ('glucide', models.IntegerField()),
                ('synopsis', models.TextField(max_length=400)),
                ('category', models.ForeignKey(to='core.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
