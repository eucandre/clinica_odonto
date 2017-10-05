from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import *
from simple_history.models import HistoricalRecords
from simple_history import register

PAYMENT_MODEL=((u'CCredito','CCredito'),(u'CDebito', 'CDebito'),
               (u'Boleto', 'Boleto'), (u'Dinheiro', 'Dinheiro'),
                (u'Cheque','Cheque'))

TYPE_PLANE = ((u'Plano', 'Plano'), (u'Avulso','Avulso'))

FUNCTION = ((u'Gerente','Gerente'),(u'Zelador(a)','Zelador(a)'),
            (u'Atendente', 'Atendente'), (u'Vigia','Vigia'),
            (u'Seguranca', 'Seguranca'))

TYPE_PROFESSIONAL = ((u'Dentista', 'Dentista'), (u'Nutricionista', 'Nutricionista'), (u'Psicologo', 'Psicologo'))

SEXO = ((u'Masculino','Masculino'),(u'Feminino','Feminino'))


class Profissionais(models.Model):

    name = models.CharField(max_length=150, unique = True)
    professional_as = models.CharField(max_length=150, choices=TYPE_PROFESSIONAL)
    salary = models.FloatField()
    sex = models.CharField(max_length=150, choices=SEXO)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    register = models.CharField(max_length=150)
    cep = models.CharField(max_length=9)
    birth_day = models.DateField()
    note = models.TextField()
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.name

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value    

    class Meta:
        verbose_name_plural = "Profissionais"

class Funcionario(models.Model):

    name = models.CharField(max_length=150,  unique = True)
    date_entry = models.DateField()
    sex = models.CharField(max_length=150,choices=SEXO)
    function = models.CharField(max_length=150, choices = FUNCTION)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11,blank=True)
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    rg = models.CharField(max_length=25, unique= True)
    cpf = models.CharField(max_length=11, unique=True)
    cep = models.CharField(max_length=9)
    birth_day = models.DateField()
    note = models.TextField()
    salary = models.FloatField()
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)
    history = HistoricalRecords()




    def __unicode__(self):
        return self.name

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value    
    

    class Meta:
        verbose_name_plural = 'Funcionarios'

class Cliente(models.Model):

    name = models.CharField(max_length=150, unique = True)
    sex = models.CharField(max_length=150,choices=SEXO)
    date_register = models.DateField(help_text='A data sugerida para pagamento mensal!')
    profession = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    cep = models.CharField(max_length=9)
    rg = models.CharField(max_length=25, unique= True)
    cpf = models.CharField(max_length=11, unique=True)
    birth_day = models.DateField()
    Note = models.TextField(blank=True)
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
        verbose_name_plural = 'Clientes'

class Cotatos_Clientes_indicacoes(models.Model):

    name = models.CharField(max_length=150, unique=True)
    sex = models.CharField(max_length=150,choices=SEXO)
    phone = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    cliente = models.BooleanField()
    indicado_por = models.ForeignKey(Cliente)
    user = models.ForeignKey(User)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.name

    @property
    def _history_user(self):
        return self.user

    @_history_user.setter
    def _history_user(self, value):
        self.user = value
    

    class Meta:
        verbose_name_plural = 'Indicados'

