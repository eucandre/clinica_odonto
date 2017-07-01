from __future__ import unicode_literals
from app_base.models import *
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

    def format_date(self):
        self.date_today = datetime.today().day
        return self.date_today


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

class RecebimentoPlanoOdonto(models.Model):
    """
        Na views ou no form elaborar uma funcao para determinar se serah cobrado jurus.
    """
    name_client = models.ForeignKey(Contrato_odonto)
    date_payment = models.DateField(auto_now=True)
    payment_for_the_month = models.DateField()
    amount_receivedD = models.FloatField(blank=True)
    amount_receivedCC = models.FloatField(blank=True)
    amount_receivedCD = models.FloatField(blank=True)
    amount_receivedB = models.FloatField(blank=True)
    amount_receiveCH = models.FloatField(blank=True)
    amount_receivePR = models.FloatField(blank=True)
    leftover_value = models.FloatField(blank=True)
    type_of_payment = models.ManyToManyField(Tipo_Recebimento)
    user = models.ForeignKey(User)

    def getMes(self):
        self.date_today = datetime.today().month
        return self.date_payment

    def __unicode__(self):
        return self.name_client.__str__()

class RecebimentoPlanoPsico(models.Model):
    """
        Na views ou no form elaborar uma funcao para determinar se serah cobrado jurus.
    """
    name_client = models.ForeignKey(Contrato_psicologo)
    date_payment = models.DateField(auto_now=True)
    payment_for_the_month = models.DateField()
    amount_receivedD = models.FloatField(blank=True)
    amount_receivedCC = models.FloatField(blank=True)
    amount_receivedCD = models.FloatField(blank=True)
    amount_receivedB = models.FloatField(blank=True)
    amount_receiveCH = models.FloatField(blank=True)
    amount_receivePR = models.FloatField(blank=True)
    leftover_value = models.FloatField(blank=True)
    type_of_payment = models.ManyToManyField(Tipo_Recebimento)
    user = models.ForeignKey(User)

    def getMes(self):
        self.date_today = datetime.today().month
        return self.date_payment

    def __unicode__(self):
        return self.name_client.__str__()

class RecebimentoPlanoNutri(models.Model):
    """
        Na views ou no form elaborar uma funcao para determinar se serah cobrado jurus.
    """
    name_client = models.ForeignKey(Contrato_nutricionista)
    date_payment = models.DateField(auto_now=True)
    payment_for_the_month = models.DateField()
    amount_receivedD = models.FloatField(blank=True)
    amount_receivedCC = models.FloatField(blank=True)
    amount_receivedCD = models.FloatField(blank=True)
    amount_receivedB = models.FloatField(blank=True)
    amount_receiveCH = models.FloatField(blank=True)
    amount_receivePR = models.FloatField(blank=True)
    leftover_value = models.FloatField(blank=True)
    type_of_payment = models.ManyToManyField(Tipo_Recebimento)
    user = models.ForeignKey(User)

    def getMes(self):
        self.date_today = datetime.today().month
        return self.date_payment

    def __unicode__(self):
        return self.name_client.__str__()
