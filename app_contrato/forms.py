from django import forms
from .models import *
import datetime
from django.forms.extras.widgets import SelectDateWidget

DAY = ((u'1','1'),(u'2','2'),(u'3','3'),(u'4','4'),(u'5','5'),(u'6','6'),(u'7','7'),(u'8','8'),(u'9','9'),(u'10','10'),
       (u'11','11'),(u'12','12'),(u'13','13'),(u'14', '14'),(u'15','15'),(u'16','16'),
       (u'17','17'),(u'18','18'),(u'19','19'),(u'20','20'),(u'21','21'),(u'22','22'),(u'23','23'),(u'24','24'),(u'25','25'),(u'26','26'),
       (u'27', '27'),(u'28','28'),(u'29','29'),(u'30','30'),(u'31','31'),)

class FormContratoOdonto(forms.ModelForm):

    propose = forms.ModelChoiceField(label="Proposta de orcamento", queryset=OrcamentoPlanoOdontologico.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    professional = forms.ModelChoiceField(label="Nome do Profissional responsavel pelo tratamento",queryset=Profissionais.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    time_contract =forms.DateField(label='Data de encerramento do tratamento' ,widget=forms.SelectDateWidget(attrs={'class':'add-on input-group-addon daterangepicker xdisplay picker_1 single opensright show-calendar', "data-inputmask":"'mask': '99/99/9999'"}))
    type_plane = forms.ChoiceField(label='Tipo de vinculo',choices=TYPE_PLANE, widget=forms.Select(attrs={'class':'form-control'}))
    plane_value = forms.CharField(label="Valor do plano",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    date_payment_per_month = forms.ChoiceField(label='Dia de vencimento mensal',choices=DAY ,widget=forms.Select(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    input_value = forms.CharField(label="Valor de entrada pago",max_length=150, initial=0, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12', 'placeholder':'R$'}))
    active = forms.BooleanField(label='Ativo na clinica ?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    note = forms.CharField(label='Observacao',widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model= Contrato_odonto
        fields = ('propose','professional','time_contract','type_plane','plane_value','date_payment_per_month',
                  'input_value','active','note')

class FormContratoNutri(forms.ModelForm):

    propose = forms.ModelChoiceField(label="Proposta de orcamento", queryset=OrcamentoPlanoNutri.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(label="Nome do Profissional responsavel pelo tratamento",queryset=Profissionais.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    time_contract =forms.DateField(label='Data de encerramento do tratamento' ,widget=forms.SelectDateWidget(attrs={'class':'add-on input-group-addon daterangepicker xdisplay picker_1 single opensright show-calendar', "data-inputmask":"'mask': '99/99/9999'"}))
    type_plane = forms.ChoiceField(label='Tipo de vinculo',choices=TYPE_PLANE, widget=forms.Select(attrs={'class':'form-control'}))
    plane_value = forms.CharField(label="Valor do plano",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    date_payment_per_month = forms.ChoiceField(label='Dia de vencimento mensal',choices=DAY ,widget=forms.Select(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    input_value = forms.CharField(label="Valor de entrada pago",max_length=150,initial=0, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    active = forms.BooleanField(label='Ativo na clinica ?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    note = forms.CharField(label='Observacao',widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model= Contrato_nutricionista
        fields = ('propose','professional','time_contract','type_plane','plane_value','date_payment_per_month',
                  'input_value','active','note')

class FormContratoPsico(forms.ModelForm):

    propose = forms.ModelChoiceField(label="Proposta de orcamento", queryset=OrcamentoPlanoPsico.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(label="Nome do Profissional responsavel pelo tratamento",queryset=Profissionais.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    time_contract =forms.DateField(label='Data de encerramento do tratamento' ,widget=forms.SelectDateWidget(attrs={'class':'add-on input-group-addon daterangepicker xdisplay picker_1 single opensright show-calendar', "data-inputmask":"'mask': '99/99/9999'"}))
    type_plane = forms.ChoiceField(label='Tipo de vinculo',choices=TYPE_PLANE, widget=forms.Select(attrs={'class':'form-control'}))
    plane_value = forms.CharField(label="Valor do plano",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    date_payment_per_month = forms.ChoiceField(label='Dia de vencimento mensal', choices=DAY ,widget=forms.Select(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    input_value = forms.CharField(label="Valor de entrada pago",max_length=150,initial=0, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    active = forms.BooleanField(label='Ativo na clinica ?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    note = forms.CharField(label='Observacao',widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model= Contrato_psicologo
        fields = ('propose','professional','time_contract','type_plane','plane_value','date_payment_per_month',
                  'input_value','active','note')

class FormRecebimentoPlano(forms.ModelForm):
    name_client=forms.ModelChoiceField(label="Nome do Cliente",queryset=Contrato_odonto.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    payment_for_the_month = forms.DateField(label='Recebimento referente a data', widget=forms.DateInput(
        attrs={'class': 'form-control', "data-inputmask": "'mask': '99/99/9999'"}))
    amount_receivedD=forms.CharField(initial=0,label="Valor pago em dinheiro",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedCC=forms.CharField(initial=0,label="Valor pago em cartao credito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedCD=forms.CharField(initial=0,label="Valor pago em cartao debito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedB=forms.CharField(initial=0,label="Valor pago em boleto",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receiveCH=forms.CharField(initial=0,label="Valor pago em cheque",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivePR=forms.CharField(initial=0,label="Valor pago sobra promissoria",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    type_of_payment = forms.MultipleChoiceField(label='Modo de pagamento', choices=PAYMENT_MODEL,widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))

    class Meta:
        model = RecebimentoPlanoOdonto
        fields = ('name_client', 'amount_receivedD','payment_for_the_month','amount_receivedCC','amount_receivedCD','amount_receivedB','amount_receiveCH'
                  ,'amount_receivePR','type_of_payment')

class FormRecebimentoPlanoPsico(forms.ModelForm):
    name_client=forms.ModelChoiceField(label="Nome do Cliente",queryset=Contrato_psicologo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    payment_for_the_month = forms.DateField(label='Recebimento referente a data', widget=forms.DateInput(
        attrs={'class': 'form-control', "data-inputmask": "'mask': '99/99/9999'"}))
    amount_receivedD=forms.CharField(initial=0,label="Valor pago em dinheiro",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedCC=forms.CharField(initial=0,label="Valor pago em cartao credito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedCD=forms.CharField(initial=0,label="Valor pago em cartao debito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedB=forms.CharField(initial=0,label="Valor pago em boleto",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receiveCH=forms.CharField(initial=0,label="Valor pago em cheque",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivePR=forms.CharField(initial=0,label="Valor pago sobra promissoria",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    type_of_payment = forms.MultipleChoiceField(label='Modo de pagamento', choices=PAYMENT_MODEL,widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))

    class Meta:
        model = RecebimentoPlanoPsico
        fields = ('name_client', 'amount_receivedD','payment_for_the_month','amount_receivedCC','amount_receivedCD','amount_receivedB','amount_receiveCH'
                  ,'amount_receivePR','type_of_payment')

class FormRecebimentoPlanoNutri(forms.ModelForm):
    name_client=forms.ModelChoiceField(label="Nome do Cliente",queryset=Contrato_nutricionista.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    payment_for_the_month = forms.DateField(label='Recebimento referente a data', widget=forms.DateInput(
        attrs={'class': 'form-control', "data-inputmask": "'mask': '99/99/9999'"}))
    amount_receivedD=forms.CharField(initial=0,label="Valor pago em dinheiro",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedCC=forms.CharField(initial=0,label="Valor pago em cartao credito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedCD=forms.CharField(initial=0,label="Valor pago em cartao debito",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivedB=forms.CharField(initial=0,label="Valor pago em boleto",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receiveCH=forms.CharField(initial=0,label="Valor pago em cheque",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    amount_receivePR=forms.CharField(initial=0,label="Valor pago sobra promissoria",max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    type_of_payment = forms.MultipleChoiceField(label='Modo de pagamento', choices=PAYMENT_MODEL,widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))

    class Meta:
        model = RecebimentoPlanoNutri
        fields = ('name_client', 'amount_receivedD','payment_for_the_month','amount_receivedCC','amount_receivedCD','amount_receivedB','amount_receiveCH'
                  ,'amount_receivePR','type_of_payment')
