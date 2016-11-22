# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0006_auto_20161030_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='currentCourse',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastestModule',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
