# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0008_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='link',
        ),
        migrations.AddField(
            model_name='component',
            name='file',
            field=models.FileField(upload_to='', default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='', default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='component',
            name='text_content',
            field=models.TextField(blank=True),
        ),
    ]
