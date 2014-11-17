# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(default=None, null=True, upload_to=b'')),
                ('custom', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=63)),
                ('gender', models.CharField(default=b'boy', max_length=4, choices=[(b'boy', b'boy'), (b'girl', b'girl')])),
                ('avatar', models.ImageField(default=None, null=True, upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=511)),
                ('password', models.CharField(max_length=63)),
                ('role', models.CharField(default=b'guardian', max_length=8, choices=[(b'mom', b'mom'), (b'dad', b'dad'), (b'guardian', b'guardian')])),
                ('avatar', models.ImageField(default=None, null=True, upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
