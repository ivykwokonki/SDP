# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0009_auto_20161124_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(upload_to='', blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='', blank=True, max_length=30),
        ),
    ]
