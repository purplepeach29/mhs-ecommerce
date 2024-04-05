# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2023-12-15 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=2000, max_digits=20),
        ),
    ]
