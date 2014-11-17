# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChopChore', '0003_parentactivitylog_device_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentactivitylog',
            name='log_file',
        ),
    ]
