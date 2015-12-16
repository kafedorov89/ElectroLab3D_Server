# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0024_auto_20151207_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfieldparam',
            name='user',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userfieldparam',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='usercoursestate',
            unique_together=set([('course', 'user')]),
        ),
    ]