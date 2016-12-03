# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0012_auto_20161124_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='text_content',
            field=models.TextField(null=True),
        ),
    ]
