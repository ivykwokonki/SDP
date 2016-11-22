# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0004_auto_20161029_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': ('is_instructor', 'is_HR', 'is_admin'), 'verbose_name': 'AB User'},
        ),
    ]
