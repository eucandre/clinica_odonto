# coding=utf-8
from django import forms
from app_estoque.models import *

TYPE_PRODUCT = ((u'Limpeza', 'Limpeza'), (u'Escritorio', 'Escritorio')
                , (u'Informatica', 'Informatica'), (u'Bucal profissional', 'Bucal profissional'),
                (u'Bucal venda', 'Bucal venda'))


class FormInsererFornecedor(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    type_product = forms.ChoiceField(label='Fornece produtos de ', choices=TYPE_PRODUCT, widget=forms.RadioSelect(attrs={'class': 'flat'}))
    cnpj = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    social_name = forms.CharField(label='Razão social',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    fantasy_name = forms.CharField(label='Nome fantasia', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    matrix = forms.CharField(label='Local da sede',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    phone = forms.CharField(label='Telefone para contato',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    site = forms.CharField(label='Endereco de página web',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'placeholder':'www.sitedofornecedor.com.br'}))
    state_registration = forms.CharField(label='Registro estadual',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    note = forms.CharField(label='Observação',widget=forms.Textarea(attrs={"class":"form-control"}))
    active = forms.BooleanField(required=False,label='Fornecedor ativo?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))

    class Meta:
        model = Fornecedor
        fields = ('name','type_product','cnpj','social_name','fantasy_name','matrix','phone','site','state_registration','note','active')

class FormInsereProduto(forms.ModelForm):

    name = forms.CharField(label='Nome', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    mark = forms.CharField(label='Marca', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    provider = forms.ModelMultipleChoiceField(label='Fornecedor',queryset=Fornecedor.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'flat'}))
    product_type = forms.ChoiceField(label='Tipo de produto', choices=TYPE_PRODUCT,widget=forms.RadioSelect(attrs={'class': 'flat'}))
    active = forms.BooleanField(required=False,label='Produto ativo?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))

    class Meta:
        model = Produto
        fields = ('name', 'mark', 'provider', 'product_type', 'active')

class FormInsereRetiraProduto(forms.ModelForm):
    product = forms.ModelChoiceField(label='Produto', queryset=Produto.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    date_for_withdrawal = forms.DateField(label='Data da retirada',widget=forms.DateInput(attrs={'type':'date','class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    time_for_withdrawal = forms.TimeField(label='Hora da retirada',widget=forms.TimeInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    amount_withdrawal = forms.FloatField(label='Quantidade retirada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    amout_refresh = forms.CharField(label='Quantidade atualizada no estoque', widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = Retira_Produto
        fields = ('product','date_for_withdrawal','time_for_withdrawal','amount_withdrawal','amout_refresh')

class FormInsereCompraProdutos(forms.ModelForm):
    product = forms.ModelChoiceField(label='Produto', queryset=Produto.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    purchase_date_product= forms.DateField(label='Data da compra',widget=forms.DateInput(attrs={'type':'date','class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    value_per_unit_to_buy = forms.FloatField(label='Valor por unidade comprada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    amout_purchased = forms.FloatField(label='Quantidade comprada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    date_vaidate = forms.DateField(label='Data da validade do produto',widget=forms.DateInput(attrs={'type':'date','class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))

    class Meta:
        model = Compra_Produto
        fields = ('product','purchase_date_product','value_per_unit_to_buy','amout_purchased','date_vaidate')

class FormMontante(forms.ModelForm):

    montante = forms.CharField(label='Montante',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    class Meta:
        model = Montante
        fields = ('montante',)