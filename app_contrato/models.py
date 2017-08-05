from __future__ import unicode_literals
from app_base.models import *
from app_receita.models import *
from django.contrib.auth.models import *

TIPO_PLANO = ((u'Odonto', 'Odonto'), (u'Nutri', 'Nutri'), (u'Psico', 'Psico'),(u'Full', 'Full'))


class Contrato_Empresa(models.Model):

    name_employe = models.CharField(max_length=150)
    social_name = models.CharField(max_length=150)
    type_plane = models.CharField(max_length=6, choices=TIPO_PLANO)
    cnpj = models.CharField(max_length=21)
    value_contract = models.FloatField(blank=True)#Este campo eh para ser preenchido caso a empresa pague todos os plano, caso nao fica para cada associado.
    discont_in_plane_associates = models.FloatField(help_text='Preecha esse campo para o desconto para associados', blank=True) #desconto para os assiciados casso tenha.ou desconto no plano
    contract_date = models.DateField(auto_now=True,unique_for_date=True)
    active = models.BooleanField(blank=True)
    note = models.TextField()

    def __unicode__(self):
        return self.name_employe

    class Meta:
        verbose_name_plural = 'Contrato Empresa'

class Contrato_Filiado_A_Empresa(models.Model):

    name = models.CharField(max_length=150, unique=True)
    associate = models.ForeignKey(Contrato_Empresa)
    professional = models.ForeignKey(Profissionais)
    registration = models.CharField(max_length=150, blank=True, unique=True)
    type_plane = models.CharField(max_length=150, choices=TYPE_PLANE, blank=True)
    date_today = models.DateField(auto_now=True,unique_for_date=True)
    date_payment_per_month = models.CharField(blank=True,max_length=2, help_text="O dia do vencimento para o mes.")
    active = models.BooleanField(blank=True)

    image_register = models.ImageField(
        null=True,
        blank=True,
        upload_to='/imagem_contrato_odonto/',
    )
    note = models.TextField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contrato de filiacao a empresa'


class Contrato_odonto(models.Model):

    propose = models.ForeignKey(Orcamento_Plano_Odonto)
    professional = models.ForeignKey(Profissionais)
    date_today = models.DateField(auto_now=True)
    time_contract = models.DateField(blank=True, help_text='Data para finalizar o tratamento')
    type_plane = models.CharField(max_length=150, choices=TYPE_PLANE)
    plane_value = models.FloatField()
    value_per_mounth = models.FloatField()
    date_payment_per_month = models.CharField(max_length=2, help_text="O dia do vencimento para o mes.")
    input_value = models.FloatField(blank=True,
                                    help_text='Valor dado de entrada, pode deixar em branco caso fique sem a entrada!')
    image_register = models.ImageField(upload_to='documents/contratos/%Y/%m/%d',blank=True)
    note = models.TextField()
    user = models.ForeignKey(User)
    active = models.BooleanField(blank=True)
    cortesia = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.propose.__unicode__()

    def value_tratment(self):
        return self.plane_value.__int__()

    def format_date(self):
        self.date_today = datetime.today().day
        return self.date_today

    def format_monts(self):
        self.date_today=datetime.today().month
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

    def format_date(self):
        self.date_today = datetime.today().day
        return self.date_today

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

    def format_date(self):
        self.date_today = datetime.today().day
        return self.date_today

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

    def TotalPagoTratamento(self):
        '''Este metodo retonara a porcentagem que representa do valor total e o que sobra para completar esse valor
            a formula eh (valorPago*100)/totalPlano =>80 
        '''
        valorOriginal= self.name_client.plane_value
        valorPago = valorOriginal-self.leftover_value
        return (valorPago*100)/valorOriginal

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

