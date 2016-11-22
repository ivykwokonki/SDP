# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDP_API', '0002_auto_20161029_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursehistroy',
            old_name='username',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='username',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ABuserID',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='ABusername',
            field=models.CharField(serialize=False, default='ABstaff0', max_length=8, primary_key=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='module',
            field=models.ForeignKey(to='SDP_API.Module'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(to='SDP_API.Course'),
        ),
    ]
