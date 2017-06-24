from __future__ import unicode_literals
import app_base.models
from app_receita.models import *
from django.contrib.auth.models import *


class Contrato_odonto(models.Model):

    propose = models.ForeignKey(OrcamentoPlanoOdontologico)
    professional = models.ForeignKey(Profissionais)
    date_today = models.DateField(auto_now=True)
    time_contract = models.DateField(blank=True, help_text='Data para finalizar o tratamento')
    type_plane = models.CharField(max_length=150, choices=TYPE_PLANE)
    plane_value = models.FloatField()
    date_payment_per_month = models.CharField(max_length=2, help_text="O dia do vencimento para o mes.")
    input_value = models.FloatField(blank=True,
                                    help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')
    note = models.TextField()
    user = models.ForeignKey(User)
    active = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.propose.__unicode__()

    def value_tratment(self):
        return self.plane_value.__int__()

class Contrato_nutricionista(models.Model):

    propose = models.ForeignKey(OrcamentoPlanoNutri)
    professional = models.ForeignKey(Profissionais)
    date_today = models.DateField(auto_now=True)
    time_contract = models.DateField(blank=True, help_text='Data para finalizar o tratamento')
    type_plane = models.CharField(max_length=150, choices=TYPE_PLANE)
    plane_value = models.FloatField()
    date_payment_per_month = models.CharField(max_length=2, help_text="O dia do vencimento para o mes.")
    input_value = models.FloatField(blank=True,
                                    help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')
    note = models.TextField()
    user = models.ForeignKey(User)
    active = models.BooleanField(blank=True)
    def __unicode__(self):
        return self.propose.__unicode__()


class Contrato_psicologo(models.Model):

    propose = models.ForeignKey(OrcamentoPlanoPsico)
    professional = models.ForeignKey(Profissionais)
    date_today = models.DateField(auto_now=True)
    time_contract = models.DateField(blank=True, help_text='Data para finalizar o tratamento')
    type_plane = models.CharField(max_length=150, choices=TYPE_PLANE)
    plane_value = models.FloatField()
    date_payment_per_month = models.CharField(max_length=2, help_text="O dia do vencimento para o mes.")
    input_value = models.FloatField(blank=True,
                                    help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')
    note = models.TextField()
    user = models.ForeignKey(User)
    active = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.propose.__unicode__()
