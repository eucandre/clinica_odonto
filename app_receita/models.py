# coding=utf-8
from __future__ import unicode_literals
from app_base.models import *
from datetime import *
from django.contrib.auth.models import *

PAYMENT_MODEL = ((u'CCredito', 'CCredito'),
                 (u'CDebito', 'CDebito'),
                 (u'Boleto', 'Boleto'),
                 (u'Dinheiro', 'Dinheiro'),
                 (u'Cheque', 'Cheque'),
                 (u'Promissoria', 'Promissoria'))

FACES_TOOTH = ((u'Mesial', 'Mesial'),
               (u'Distal', 'Distal'),
               (u'Oclusal', 'Oclusal'),
               (u'Vestibular', 'Vestibular'),
               (u'Lingual', 'Lingual'),
               (u'Incisal', 'Incisal'),
               (u'Platina', 'Platina'))

TYPE_PLANE = ((u'Plano', 'Plano'), (u'Avulso', 'Avulso'))

TOOTH = (
    (u'1', '1'), (u'2', '2'), (u'3', '3'), (u'4', '4'), (u'5', '5'), (u'6', '6'), (u'7', '7'), (u'8', '8'), (u'9', '9'),
    (u'10', '10'), (u'11', '11'), (u'12', '12'), (u'13', '13'), (u'14', '14'), (u'15', '15'), (u'16', '16'),
    (u'17', '17'),(u'18', '18'), (u'19', '19'), (u'20', '20'), (u'21', '21'), (u'22', '22'), (u'23', '23'),
    (u'24', '24'),(u'25', '25'), (u'26', '26'), (u'27', '27'), (u'28', '28'), (u'29', '29'), (u'30', '30'),
    (u'31', '31'),(u'32', '32'), (u'33', '33'), (u'34', '34'), (u'35', '35'), (u'36', '36'), (u'37', '37'),
    (u'38', '38'),(u'39', '39'),)

class Servicos(models.Model):

    name =models.CharField(max_length=150)
    cost = models.FloatField()
    odonto = models.BooleanField(blank=True)
    nutri = models.BooleanField(blank=True)
    pscico = models.BooleanField(blank=True)
    professional = models.ManyToManyField(Profissionais, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Serviços'

class Dentes(models.Model):
    number_tooth = models.CharField(max_length=150, choices=TOOTH)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.number_tooth

    class Meta:
        verbose_name_plural = "Dente"

class Tipo_Recebimento(models.Model):

    type_payment = models.CharField(max_length=150, choices=PAYMENT_MODEL)

    def __unicode__(self):
        return self.type_payment

    class Meta:
        verbose_name_plural = "Tipo de Recebimento"

class FacesDentes(models.Model):
    face = models.CharField(max_length=20, choices=FACES_TOOTH)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.face

    class Meta:
        verbose_name_plural = "Faces do Dente"

class Orcamento_Plano_Odonto(models.Model):

    name_client = models.ForeignKey(Cliente)
    tooths = models.ManyToManyField(Dentes)
    faces_tooths = models.ManyToManyField(FacesDentes)
    date_today = models.DateField(auto_now=True)
    date_to_end_tratment = models.DateField()
    services = models.ManyToManyField(Servicos)
    value_tratment = models.FloatField()
    note = models.TextField(blank=True)
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_client.__unicode__()

    def format_date(self):
        self.date_today = datetime.today().month
        return self.date_today

    def plane_value(self):
        return self.value_tratment.__int__()

    class Meta:
        verbose_name_plural = "Orçamento Plano Odontonlógico"

class OrcamentoPlanoNutri(models.Model):

    name_client = models.ForeignKey(Cliente)
    date_today = models.DateField(auto_now=True)
    date_to_end_tratment = models.DateField()
    services = models.ManyToManyField(Servicos, blank=True)
    value_tratment = models.FloatField()
    note = models.TextField(blank=True)
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_client.__str__()

    def format_date(self):
        self.date_today = datetime.today().day
        return self.date_today

    class Meta:
        verbose_name_plural = "Orcamento Plano Nutricionista"

class OrcamentoPlanoPsico(models.Model):
    name_client = models.ForeignKey(Cliente)
    date_today = models.DateField(auto_now=True)
    date_to_end_tratment = models.DateField()
    services = models.ManyToManyField(Servicos, blank=True)
    value_tratment = models.FloatField()
    note = models.TextField(blank=True)
    active = models.BooleanField(blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_client.__str__()

    def format_date(self):
        self.date_today = datetime.today().day
        return self.date_today

    def format_months(self):
        self.date_today = datetime.today().month
        return self.date_today

    class Meta:
        verbose_name_plural = "Orcamento Plano Psicológico"

class RecebimentoAvulso(models.Model):
    """
        Esta classe eh para pagamento de tratamentos avulsos, sem plano!
    """
    name_client = models.ForeignKey(Cliente)
    date_attendance = models.DateField()
    payment_for_the_month = models.DateField()
    services = models.ManyToManyField(Servicos, blank=True)
    value_tratment = models.FloatField()
    professional_attendance = models.ForeignKey(Profissionais)
    value_attendanceD = models.FloatField(blank=True)
    value_attendanceCC = models.FloatField(blank=True)
    value_attendanceCD = models.FloatField(blank=True)
    value_attendanceB = models.FloatField(blank=True)
    amount_receivePR = models.FloatField(blank=True)
    leftover_value = models.FloatField(blank=True)
    note = models.TextField(blank=True)
    type_of_payment = models.ManyToManyField(Tipo_Recebimento)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_client.__str__()

    class Meta:
        verbose_name_plural = 'Recebimento Plano a vulso'