from __future__ import unicode_literals

from django.db import models
from app_base.models import *
from django.contrib.auth.models import *

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
    active = models.BooleanField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class Produto( models.Model):
    '''
        Os valores dessa classe serao atualizados mediante a manipulacao das classes de Retirada e a de compra
    '''
    name = models.CharField(max_length=150)
    mark = models.CharField(max_length=150)
    provider = models.ManyToManyField(Fornecedor)
    amount = models.FloatField()
    value_per_unit_to_buy = models.FloatField()
    purchase_date = models.DateField()
    date_vaidate = models.DateField()
    product_type =models.CharField(max_length=150, choices=TYPE_PRODUCT)
    active = models.BooleanField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Produtos'
        
class Retira_Produto(models.Model):

    product = models.ForeignKey(Produto)
    date_for_withdrawal = models.DateTimeField()
    amount_withdrawal = models.FloatField()
    responsible = models.ForeignKey(Funcionario)
    amout_refresh = models.CharField(max_length=150)# Sera atualizada pelo formulario
    user = models.ForeignKey(User)

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

    def __unicode__(self):
        return self.product.__str__()

    class Meta:
        verbose_name_plural = 'Compra produtos'