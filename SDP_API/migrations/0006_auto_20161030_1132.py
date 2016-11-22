# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0005_auto_20161030_0728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'AB User'},
        ),
        migrations.AddField(
            model_name='component',
            name='name',
            field=models.CharField(default='component', max_length=100),
        ),
    ]
