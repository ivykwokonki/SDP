# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0019_auto_20161124_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='file',
            field=models.FileField(upload_to='', null=True, default=None),
        ),
        migrations.AddField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='', null=True, default=None),
        ),
        migrations.AddField(
            model_name='component',
            name='text_content',
            field=models.TextField(null=True, default=None),
        ),
    ]
