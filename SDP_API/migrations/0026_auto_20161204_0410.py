# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0025_auto_20161204_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursehistroy',
            name='completed_at',
            field=models.DateTimeField(),
        ),
    ]
