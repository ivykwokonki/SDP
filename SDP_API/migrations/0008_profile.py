# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('SDP_API', '0007_auto_20161030_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('ABusername', models.CharField(max_length=8, default='ABstaff0')),
                ('currentCourse', models.IntegerField(default=-999)),
                ('latestModule', models.IntegerField(default=-999)),
            ],
            options={
                'verbose_name': 'AB User',
            },
        ),
    ]
