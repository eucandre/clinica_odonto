# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-01 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='date_vaidate',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='value_per_unit_to_buy',
        ),
    ]
