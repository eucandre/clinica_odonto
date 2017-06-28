# -*- coding: utf-8 -*-

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
            name='Dentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_tooth', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39')], max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FacesDentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.CharField(choices=[('Mesial', 'Mesial'), ('Distal', 'Distal'), ('Oclusal', 'Oclusal'), ('Vestibular', 'Vestibular'), ('Lingual', 'Lingual'), ('Incisal', 'Incisal'), ('Platina', 'Platina')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoPlanoNutri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now=True)),
                ('date_to_end_tratment', models.DateField()),
                ('value_tratment', models.FloatField()),
                ('active', models.BooleanField()),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoPlanoOdontologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now=True)),
                ('date_to_end_tratment', models.DateField()),
                ('value_tratment', models.FloatField()),
                ('active', models.BooleanField()),
                ('faces_tooths', models.ManyToManyField(to='app_receita.FacesDentes')),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('tooths', models.ManyToManyField(to='app_receita.Dentes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrcamentoPlanoPsico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_today', models.DateField(auto_now=True)),
                ('date_to_end_tratment', models.DateField()),
                ('value_tratment', models.FloatField()),
                ('active', models.BooleanField()),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoAvulso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attendance', models.DateField()),
                ('payment_for_the_month', models.DateField()),
                ('value_attendanceD', models.FloatField(blank=True)),
                ('value_attendanceCC', models.FloatField(blank=True)),
                ('value_attendanceCD', models.FloatField(blank=True)),
                ('value_attendanceB', models.FloatField(blank=True)),
                ('amount_receivePR', models.FloatField(blank=True)),
                ('leftover_value', models.FloatField(blank=True)),
                ('type_of_payment', models.CharField(max_length=150)),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('professional_attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Profissionais')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoPlano',
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
                ('type_of_payment', models.CharField(choices=[('CCredito', 'CCredito'), ('CDebito', 'CDebito'), ('Boleto', 'Boleto'), ('Dinheiro', 'Dinheiro'), ('Cheque', 'Cheque'), ('Promissoria', 'Promissoria')], max_length=150)),
                ('name_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Recebimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_payment', models.CharField(choices=[('CCredito', 'CCredito'), ('CDebito', 'CDebito'), ('Boleto', 'Boleto'), ('Dinheiro', 'Dinheiro'), ('Cheque', 'Cheque'), ('Promissoria', 'Promissoria')], max_length=150)),
            ],
        ),
    ]
