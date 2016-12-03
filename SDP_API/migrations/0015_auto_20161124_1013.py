# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0014_auto_20161124_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='', blank=True),
        ),
    ]
