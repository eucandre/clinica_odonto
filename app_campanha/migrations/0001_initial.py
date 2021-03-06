# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 01:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='campanha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_initi', models.DateField(auto_now=True)),
                ('date_end', models.DateField()),
                ('reward', models.CharField(blank=True, max_length=150)),
                ('reward1', models.CharField(blank=True, max_length=150)),
                ('reward2', models.CharField(blank=True, max_length=150)),
                ('reward3', models.CharField(blank=True, max_length=150)),
                ('active', models.BooleanField()),
                ('note', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='campanha_venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_sell', models.IntegerField()),
                ('note', models.TextField()),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_campanha.campanha')),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('name_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Funcionario')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
