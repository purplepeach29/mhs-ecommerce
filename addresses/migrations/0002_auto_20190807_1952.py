# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-08-07 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='India', max_length=120),
        ),
    ]