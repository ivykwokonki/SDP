# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0010_auto_20161124_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(max_length=30, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(max_length=30, null=True, upload_to=''),
        ),
    ]
