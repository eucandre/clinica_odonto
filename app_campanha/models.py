from __future__ import unicode_literals
from django.db import models
from app_base.models import *

class campanha(models.Model):
    name = models.CharField(max_length=150)
    date_initi = models.DateField(auto_now=True)
    date_end = models.DateField()
    reward = models.CharField(max_length=150, blank=True)
    reward1 = models.CharField(max_length=150, blank=True)
    reward2 = models.CharField(max_length=150, blank=True)
    reward3 = models.CharField(max_length=150, blank=True)
    active = models.BooleanField(blank=True)
    note = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

class campanha_venda(models.Model):
    campanha = models.ForeignKey(campanha)
    name_seller = models.ForeignKey(Funcionario)
    name_client = models.ForeignKey(Cliente)
    value_sell = models.IntegerField()
    note = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_seller.__unicode__()

