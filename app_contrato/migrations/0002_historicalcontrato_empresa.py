# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-27 02:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_contrato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalContrato_Empresa',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name_employe', models.CharField(max_length=150)),
                ('social_name', models.CharField(max_length=150)),
                ('type_plane', models.CharField(choices=[('Odonto', 'Odonto'), ('Nutri', 'Nutri'), ('Psico', 'Psico'), ('Full', 'Full')], max_length=6)),
                ('cnpj', models.CharField(max_length=21)),
                ('value_contract', models.FloatField(blank=True)),
                ('discont_in_plane_associates', models.FloatField(blank=True, help_text='Preecha esse campo para o desconto para associados')),
                ('contract_date', models.DateField(blank=True, editable=False, unique_for_date=True)),
                ('active', models.BooleanField()),
                ('note', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical contrato_ empresa',
            },
        ),
    ]
