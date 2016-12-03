# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0013_auto_20161124_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(null=True, upload_to='', max_length=30),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(null=True, upload_to='', max_length=30),
        ),
        migrations.AlterField(
            model_name='component',
            name='text_content',
            field=models.TextField(blank=True),
        ),
    ]
