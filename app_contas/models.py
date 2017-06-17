from __future__ import unicode_literals

from django.db import models

TYPE =((u'Periodica', 'Periodica'), (u'Corriqueira', 'Corriqueira'))
PRIORIDADE = ((u'Alta', 'Alta'), (u'Media', 'Media'), (u'Baixa', 'Baixa'))

class Conta_Paga(models.Model):
    pay_to = models.CharField(max_length=150)
    value_count = models.FloatField()
    date_to_payment = models.DateField(unique_for_date=True)
    frequencia = models.CharField(max_length=15, choices=TYPE)
    prioridade = models.CharField(max_length=15, choices=PRIORIDADE)

    def __unicode__(self):
        return self.pay_to
