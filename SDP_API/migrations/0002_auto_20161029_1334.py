# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='module',
            field=models.ForeignKey(to='SDP_API.Module', unique=True),
        ),
        migrations.AlterField(
            model_name='coursehistroy',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(to='SDP_API.Course', unique=True),
        ),
    ]
