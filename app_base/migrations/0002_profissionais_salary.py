# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissionais',
            name='salary',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
