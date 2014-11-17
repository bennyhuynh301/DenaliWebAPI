# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChopChore', '0002_parentactivitylog'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentactivitylog',
            name='device_id',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
