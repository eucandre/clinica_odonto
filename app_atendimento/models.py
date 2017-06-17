# -*- coding: cp1252 -*-.
from __future__ import unicode_literals
from app_receita.models import *
from app_contrato.models import *
from django.contrib.auth.models import *

AGENDAMENTO=((u'Atendimento clinico', 'Atendimento clinico'),(u'Exame clinico','Exame clinico'))

'''
    estas classes irao formar o mapa de atendimento!
'''

class relatorio_exame_odonto(models.Model):
    name_client = models.ForeignKey(Cliente)
    professional = models.ForeignKey(Profissionais)
    tooths = models.ManyToManyField(Dentes)
    faces_tooths = models.ManyToManyField(FacesDentes)
    date_atendence = models.DateField()
    date_now = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Relatorio de Exame Odonto'

class relatorio_exame_psico(models.Model):
    name_client = models.ForeignKey(Cliente)
    professional = models.ForeignKey(Profissionais)
    date_atendence = models.DateField()
    date_now = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Relatorio de Exame Psico'

class relatorio_exame_nutri(models.Model):
    name_client = models.ForeignKey(Cliente)
    professional = models.ForeignKey(Profissionais)
    date_atendence = models.DateField()
    date_now = models.DateField(auto_now=True)
    user = models.ForeignKey(User)
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Relatorio de Exame Nutri'

class agendamemto_plano_odonto(models.Model):
    name_client = models.ForeignKey(Contrato_odonto)
    atendence = models.CharField(choices=AGENDAMENTO, max_length=150)
    professional = models.ForeignKey(Profissionais)
    date_atendence = models.DateField()
    user = models.ForeignKey(User)
    active = models.BooleanField()
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__unicode__()

    def formata_date(self):
        return self.date_atendence.__str__()

    def get_date_atendence(self):        
      return self.date_atendence.__str__()

    class Meta:
        verbose_name_plural = 'Agendamento para planos odonto'

class agendamemto_plano_nutri(models.Model):
    name_client = models.ForeignKey(Contrato_nutricionista)
    atendence = models.CharField(choices=AGENDAMENTO, max_length=150)
    professional = models.ForeignKey(Profissionais)
    date_atendence = models.DateTimeField()
    user = models.ForeignKey(User)
    active = models.BooleanField()
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Agendamento para planos Nutri'

class agendamemto_plano_psico(models.Model):
    name_client = models.ForeignKey(Contrato_psicologo)
    atendence = models.CharField(choices=AGENDAMENTO, max_length=150)
    professional = models.ForeignKey(Profissionais)
    date_atendence = models.DateTimeField()
    user = models.ForeignKey(User)
    active = models.BooleanField()
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Agendamento para planos Psico'

class agendamento_simples(models.Model):
    name_client = models.ForeignKey(Cliente)
    atendence = models.CharField(choices=AGENDAMENTO, max_length=150)
    professional = models.ForeignKey(Profissionais)
    date_atendence = models.DateTimeField()
    user = models.ForeignKey(User)
    active = models.BooleanField()
    note = models.TextField()

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Agendamento simples'


