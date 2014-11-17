# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChopChore', '0004_remove_parentactivitylog_log_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentactivitylog',
            name='device_id',
        ),
        migrations.AddField(
            model_name='parentactivitylog',
            name='log_file',
            field=models.FileField(null=True, upload_to=b'/parents_log/', blank=True),
            preserve_default=True,
        ),
    ]
