# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jchat', '0002_auto_20160207_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
