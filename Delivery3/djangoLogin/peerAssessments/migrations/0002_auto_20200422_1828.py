# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-22 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='eagleid',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='eagleid',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
