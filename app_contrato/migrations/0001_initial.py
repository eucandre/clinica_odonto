# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-17 01:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_receita', '0001_initial'),
        ('app_base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato_Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_employe', models.CharField(max_length=150)),
                ('social_name', models.CharField(max_length=150)),
                ('type_plane', models.CharField(choices=[('Odonto', 'Odonto'), ('Nutri', 'Nutri'), ('Psico', 'Psico'), ('Full', 'Full')], max_length=6)),
                ('cnpj', models.CharField(max_length=21)),
                ('value_contract', models.FloatField(blank=True)),
                ('discont_in_plane_associates', models.FloatField(blank=True, help_text='Preecha esse campo para o desconto para associados')),
                ('contract_date', models.DateField(auto_now=True, unique_for_date=True)),
                ('active', models.BooleanField()),
                ('note', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contrato Empresa',
            },
        ),
        migrations.CreateModel(
            name='Contrato_Filiado_A_Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('registration', models.CharField(blank=True, max_length=150, unique=True)),
                ('type_plane', models.CharField(blank=True, choices=[('Plano', 'Plano'), ('Avulso', 'Avulso')], max_length=150)),
                ('date_today', models.DateField(auto_now=True, unique_for_date=True)),
                ('date_payment_per_month', models.CharField(blank=True, help_text='O dia do vencimento para o mes.', max_length=2)),
                ('active', models.BooleanField()),
                ('image_register', models.ImageField(blank=True, null=True, upload_to='/imagem_contrato_odonto/')),
                ('note', models.TextField()),
                ('associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_Empresa')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Profissionais')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contrato de filiacao a empresa',
            },
        ),
        migrations.CreateModel(
            name='Contrato_nutricionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now=True)),
                ('time_contract', models.DateField(blank=True, help_text='Data para finalizar o tratamento')),
                ('type_plane', models.CharField(choices=[('Plano', 'Plano'), ('Avulso', 'Avulso')], max_length=150)),
                ('plane_value', models.FloatField()),
                ('date_payment_per_month', models.CharField(help_text='O dia do vencimento para o mes.', max_length=2)),
                ('input_value', models.FloatField(blank=True, help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')),
                ('note', models.TextField()),
                ('active', models.BooleanField()),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Profissionais')),
                ('propose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_receita.OrcamentoPlanoNutri')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato_odonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now=True)),
                ('time_contract', models.DateField(blank=True, help_text='Data para finalizar o tratamento')),
                ('type_plane', models.CharField(choices=[('Plano', 'Plano'), ('Avulso', 'Avulso')], max_length=150)),
                ('plane_value', models.FloatField()),
                ('value_per_mounth', models.FloatField()),
                ('date_payment_per_month', models.CharField(help_text='O dia do vencimento para o mes.', max_length=2)),
                ('input_value', models.FloatField(blank=True, help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')),
                ('image_register', models.ImageField(blank=True, upload_to='documents/contratos/%Y/%m/%d')),
                ('note', models.TextField()),
                ('active', models.BooleanField()),
                ('cortesia', models.BooleanField()),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Profissionais')),
                ('propose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_receita.Orcamento_Plano_Odonto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato_psicologo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now=True)),
                ('time_contract', models.DateField(blank=True, help_text='Data para finalizar o tratamento')),
                ('type_plane', models.CharField(choices=[('Plano', 'Plano'), ('Avulso', 'Avulso')], max_length=150)),
                ('plane_value', models.FloatField()),
                ('date_payment_per_month', models.CharField(help_text='O dia do vencimento para o mes.', max_length=2)),
                ('input_value', models.FloatField(blank=True, help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')),
                ('note', models.TextField()),
                ('active', models.BooleanField()),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Profissionais')),
                ('propose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_receita.OrcamentoPlanoPsico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoPlanoNutri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payment', models.DateField(auto_now=True)),
                ('payment_for_the_month', models.DateField()),
                ('amount_receivedD', models.FloatField(blank=True)),
                ('amount_receivedCC', models.FloatField(blank=True)),
                ('amount_receivedCD', models.FloatField(blank=True)),
                ('amount_receivedB', models.FloatField(blank=True)),
                ('amount_receiveCH', models.FloatField(blank=True)),
                ('amount_receivePR', models.FloatField(blank=True)),
                ('leftover_value', models.FloatField(blank=True)),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_nutricionista')),
                ('type_of_payment', models.ManyToManyField(to='app_receita.Tipo_Recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoPlanoOdonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payment', models.DateField(auto_now=True)),
                ('payment_for_the_month', models.DateField()),
                ('amount_receivedD', models.FloatField(blank=True)),
                ('amount_receivedCC', models.FloatField(blank=True)),
                ('amount_receivedCD', models.FloatField(blank=True)),
                ('amount_receivedB', models.FloatField(blank=True)),
                ('amount_receiveCH', models.FloatField(blank=True)),
                ('amount_receivePR', models.FloatField(blank=True)),
                ('leftover_value', models.FloatField(blank=True)),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_odonto')),
                ('type_of_payment', models.ManyToManyField(to='app_receita.Tipo_Recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoPlanoPsico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_payment', models.DateField(auto_now=True)),
                ('payment_for_the_month', models.DateField()),
                ('amount_receivedD', models.FloatField(blank=True)),
                ('amount_receivedCC', models.FloatField(blank=True)),
                ('amount_receivedCD', models.FloatField(blank=True)),
                ('amount_receivedB', models.FloatField(blank=True)),
                ('amount_receiveCH', models.FloatField(blank=True)),
                ('amount_receivePR', models.FloatField(blank=True)),
                ('leftover_value', models.FloatField(blank=True)),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_psicologo')),
                ('type_of_payment', models.ManyToManyField(to='app_receita.Tipo_Recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
