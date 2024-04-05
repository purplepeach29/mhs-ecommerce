# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2024-04-02 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0011_auto_20240402_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='card',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
