# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'text'), (1, 'photo'), (2, 'file'), (3, 'quiz')])),
                ('link', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_opened', models.BooleanField(default=False)),
                ('orderOfModule', models.TextField(blank=True)),
                ('category', models.ForeignKey(to='SDP_API.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CourseHistroy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='SDP_API.Course')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('permission_createCourse', models.BooleanField(default=False)),
                ('permission_modifyCourse', models.BooleanField(default=False)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(to='SDP_API.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ABuserID', models.CharField(max_length=8)),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Instructor'), (1, 'Participant'), (2, 'Admin'), (3, 'HR')])),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_HR', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('currentSession', models.PositiveSmallIntegerField(default=1, choices=[(0, 'Instructor'), (1, 'Participant'), (2, 'Admin'), (3, 'HR')])),
                ('currentCourse', models.ForeignKey(null=True, to='SDP_API.Course')),
                ('lastestModule', models.ForeignKey(null=True, to='SDP_API.Module')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'AB User',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(to='SDP_API.Instructor'),
        ),
        migrations.AddField(
            model_name='component',
            name='course',
            field=models.ForeignKey(to='SDP_API.Course'),
        ),
        migrations.AddField(
            model_name='component',
            name='module',
            field=models.ForeignKey(to='SDP_API.Module'),
        ),
    ]
