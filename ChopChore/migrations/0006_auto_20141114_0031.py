# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChopChore', '0005_auto_20141114_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentactivitylog',
            name='log_file',
            field=models.FileField(default=0, upload_to=b'parents_log'),
            preserve_default=False,
        ),
    ]
