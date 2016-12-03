# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0018_auto_20161124_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='file',
        ),
        migrations.RemoveField(
            model_name='component',
            name='image',
        ),
        migrations.RemoveField(
            model_name='component',
            name='text_content',
        ),
    ]
