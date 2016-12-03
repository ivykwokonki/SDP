# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0017_auto_20161124_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='file',
            field=models.FileField(null=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(null=True, default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='component',
            name='text_content',
            field=models.TextField(null=True, default=None),
        ),
    ]
