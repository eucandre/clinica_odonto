from __future__ import unicode_literals

from django.db import models
from app_base.models import *
from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords

TYPE_PRODUCT = ((u'Limpeza','Limpeza'),(u'Escritorio','Escritorio')
,(u'Informatica','Informatica'),(u'Bucal profissional','Bucal profissional'),(u'Bucal venda','Bucal venda'))

class Fornecedor(models.Model):

    name = models.CharField(max_length=150)
    type_product = models.CharField(max_length=150, choices=TYPE_PRODUCT)
    cnpj = models.CharField(max_length=30, unique=True)
    social_name = models.CharField(max_length=150)
    fantasy_name = models.CharField(max_length=150)
    matrix = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    site = models.CharField(max_length=150, blank=True)
    state_registration = models.CharField(max_length=150)
    note = models.TextField()
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.name

class Produto( models.Model):
    '''
        Os valores dessa classe serao atualizados mediante a manipulacao das classes de Retirada e a de compra
    '''
    name = models.CharField(max_length=150)
    mark = models.CharField(max_length=150)
    provider = models.ManyToManyField(Fornecedor)
    product_type =models.CharField(max_length=150, choices=TYPE_PRODUCT)
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Produtos'
        
class Retira_Produto(models.Model):

    product = models.ForeignKey(Produto)
    date_for_withdrawal = models.DateTimeField()
    amount_withdrawal = models.FloatField()
    amout_refresh = models.CharField(max_length=150)# Sera atualizada pelo formulario
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = 'Retira produtos'

class Compra_Produto(models.Model):

    product = models.ForeignKey(Produto)
    purchase_date_product = models.DateField()
    value_per_unit_to_buy = models.FloatField()
    amout_purchased = models.FloatField()
    date_vaidate = models.DateField()
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def __unicode__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = 'Compra produtos'

class Montante(models.Model):

    montante = models.CharField(max_length=150 )#esta variavel sera atualizada no forms
    user = models.ForeignKey(User)

    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.montante is None:
            self.montante = 0

