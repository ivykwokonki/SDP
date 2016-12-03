# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0021_auto_20161128_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(null=True, upload_to='uploaded_file/', default=None),
        ),
    ]
