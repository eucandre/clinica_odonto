# coding=utf-8
from django import forms
from app_base.models import *
from app_receita.models import *

PAYMENT_MODEL=((u'CCredito','CCredito'),(u'CDebito', 'CDebito'),
               (u'Boleto', 'Boleto'), (u'Dinheiro', 'Dinheiro'),
                (u'Cheque','Cheque'))


class FormServicos(forms.BaseModelForm):
    class Meta:
        model = Servicos
        fields = '__all__'

class FormDentes(forms.ModelForm):
    number_tooth = forms.CharField(label="Numero do dente", max_length=150,widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = Dentes
        fields = ('number_tooth', )

class FormOrcamentoOdontologico(forms.ModelForm):
    name_client = forms.ModelChoiceField(label="Nome do Cliente",queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    tooths = forms.ModelMultipleChoiceField(label='Dente', queryset=Dentes.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    faces_tooths = forms.ModelMultipleChoiceField(label="Faces do dente", queryset=FacesDentes.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'flat'}))
    services = forms.ModelMultipleChoiceField(label='Serviços',queryset=Servicos.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'flat'}))
    date_to_end_tratment= forms.DateField(label='Data para o fim do tratamento',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    value_tratment = forms.CharField(label="Valor do tratamento",max_length=150, widget=forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}))
    active = forms.BooleanField(required=False,label='Ativo na clinica?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    class Meta:
        model = Orcamento_Plano_Odonto
        fields = ('name_client', 'tooths', 'faces_tooths', 'services','date_to_end_tratment', 'value_tratment', 'active')

class FormOrcamentoPlanoNutri(forms.ModelForm):
    name_client = forms.ModelChoiceField(label="Nome do Cliente",queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    date_to_end_tratment= forms.DateField(label='Data para o fim do tratamento',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    value_tratment = forms.CharField(label="Valor do tratamento",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    services = forms.ModelMultipleChoiceField(queryset=Servicos.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))
    active = forms.BooleanField(label='Ativo na clinica?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    class Meta:
        model = OrcamentoPlanoNutri
        fields = ('name_client', 'date_to_end_tratment', 'value_tratment','active')

class FormOrcamentoPlanoPsico(forms.ModelForm):
    name_client = forms.ModelChoiceField(label="Nome do Cliente",queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    date_to_end_tratment= forms.DateField(label='Data para o fim do tratamento',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    value_tratment = forms.CharField(label="Valor do tratamento",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    services = forms.ModelMultipleChoiceField(queryset=Servicos.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))
    active = forms.BooleanField(label='Ativo na clinica?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    class Meta:
        model = OrcamentoPlanoPsico
        fields = ('name_client','date_to_end_tratment','value_tratment','active')

class FormRecebimentoAvulso(forms.ModelForm):
    name_client = forms.ModelChoiceField(label="Nome do Cliente",queryset=Cliente.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    date_attendance = forms.DateField(label='Data do atendimento' ,widget=forms.DateInput(attrs={'type':'date','class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    payment_for_the_month = forms.DateField(label='Recebimento referente a data' ,widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    professional_attendance = forms.ModelChoiceField(label="Nome do Profissional que atendeu o cliente",queryset=Profissionais.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    value_attendanceD = forms.CharField(initial=0,label="Valor do tratamento pago em dinheiro",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    value_attendanceCC = forms.CharField(initial=0,label="Valor do tratamento pago em cartao de credito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    value_attendanceCD = forms.CharField(initial=0,label="Valor do tratamento pago em cartao de debito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    value_attendanceB = forms.CharField(initial=0,label="Valor do tratamento pago em boleto",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    value_attendancePR = forms.CharField(initial=0,label="Valor do tratamento sobra para promissoria",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    services = forms.ModelMultipleChoiceField(label='Serviços',queryset=Servicos.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))
    type_of_payment = forms.ModelMultipleChoiceField(label='Modos usados para pagamento',queryset=Tipo_Recebimento.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'flat'}))
    class Meta:
        model = RecebimentoAvulso
        fields = ('name_client','date_attendance','payment_for_the_month','professional_attendance', 'value_attendanceD',
                  'value_attendanceCC','value_attendanceCD','value_attendanceB','value_attendancePR', 'type_of_payment')

