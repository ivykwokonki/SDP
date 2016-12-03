# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0020_auto_20161124_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='image',
        ),
        migrations.RemoveField(
            model_name='course',
            name='orderOfModule',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ABusername',
        ),
        migrations.AddField(
            model_name='component',
            name='link',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='component',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='course',
            name='no_of_module',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='no_of_component',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='component',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'text'), (1, 'photo'), (2, 'file'), (3, 'video'), (4, 'quiz')]),
        ),
    ]
