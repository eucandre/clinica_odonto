from __future__ import unicode_literals
from app_atendimento.models import *
from django.db import models

class Perfil(models.Model):
    name = models.ForeignKey(RecebimentoPlano)


    def __unicode__(self):
        return self.name


