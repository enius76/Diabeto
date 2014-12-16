# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_food_synopsis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glyc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('firstname', models.CharField(max_length=150)),
                ('birth', models.DateField()),
                ('sexe', models.CharField(max_length=1)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('mail', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=8)),
                ('glyc', models.ForeignKey(to='core.Glyc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
