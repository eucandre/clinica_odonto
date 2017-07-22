# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contrato', '0002_contrato_odonto_cortesia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato_Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_employe', models.CharField(max_length=150)),
                ('type_plane', models.CharField(choices=[('Odonto', 'Odonto'), ('Nutri', 'Nutri'), ('Psico', 'Psico'), ('Full', 'Full')], max_length=6)),
                ('cnpj', models.CharField(max_length=21)),
                ('value_contract', models.FloatField(blank=True)),
                ('discont_in_plane_associates', models.FloatField(blank=True, help_text='Preecha esse campo para o desconto para associados')),
                ('note', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contrato Empresa',
            },
        ),
        migrations.AddField(
            model_name='contrato_odonto',
            name='image_register',
            field=models.ImageField(blank=True, null=True, upload_to='/imagem_contrato_odonto/'),
        ),
        migrations.AddField(
            model_name='contrato_odonto',
            name='value_per_mounth',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]