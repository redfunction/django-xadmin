# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-05 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190813_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='idc',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]
