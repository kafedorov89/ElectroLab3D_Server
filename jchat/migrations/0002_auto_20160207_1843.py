# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 18:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 7, 18, 43, 19, 568325, tzinfo=utc)),
        ),
    ]
