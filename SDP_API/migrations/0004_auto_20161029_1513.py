# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0003_auto_20161029_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='id',
        ),
        migrations.AlterField(
            model_name='instructor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, primary_key=True, default=1, serialize=False),
        ),
    ]
