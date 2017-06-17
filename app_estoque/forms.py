from django import forms
from app_estoque.models import *

TYPE_PRODUCT = ((u'Limpeza', 'Limpeza'), (u'Escritorio', 'Escritorio')
                , (u'Informatica', 'Informatica'), (u'Bucal profissional', 'Bucal profissional'),
                (u'Bucal venda', 'Bucal venda'))


class FormInsererFornecedor(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    type_product = forms.ChoiceField(label='Fornece produtos de ', choices=TYPE_PRODUCT, widget=forms.RadioSelect(attrs={'class': 'flat'}))
    cnpj = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    social_name = forms.CharField(label='Razao social',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    fantasy_name = forms.CharField(label='Nome fantasia', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    matrix = forms.CharField(label='Local da sede',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    phone = forms.CharField(label='Telefone para contato',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    site = forms.CharField(label='Endereco de pagina web',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12', 'placeholder':'www.google.com'}))
    state_registration = forms.CharField(label='Registro estadual',max_length=150, widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    note = forms.CharField(label='Observacao',widget=forms.Textarea(attrs={"class":"form-control"}))
    active = forms.BooleanField(label='Fornecedor ativo?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))

    class Meta:
        model = Fornecedor
        fields = ('name','type_product','cnpj','social_name','fantasy_name','matrix','phone','site','state_registration','note','active')

class FormInsereProduto(forms.ModelForm):

    name = forms.CharField(label='Nome', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    mark = forms.CharField(label='Marca', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    provider = forms.ModelMultipleChoiceField(label='Fornecedor',queryset=Fornecedor.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class':'flat'}))
    amount = forms.FloatField(label='Quantidade',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    value_per_unit_to_buy = forms.FloatField(label='Valor pago por unidade comprada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    purchase_date = forms.DateField(label='Data de registro',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    date_vaidate = forms.DateField(label='Validade do produto',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    product_type = forms.ChoiceField(label='Tipo de produto', choices=TYPE_PRODUCT,widget=forms.RadioSelect(attrs={'class': 'flat'}))

    class Meta:
        model = Produto
        fields = ('name', 'mark', 'provider', 'amount','value_per_unit_to_buy','purchase_date','date_vaidate','product_type')
class FormInsereRetiraProduto(forms.ModelForm):
    product = forms.ModelChoiceField(label='Produto', queryset=Produto.objects.all(), widget=forms.Select(attrs={'class':'flat'}))
    date_for_withdrawal = forms.DateField(label='Data da retirada',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    time_for_withdrawal = forms.TimeField(label='Hora da retirada',widget=forms.TimeInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    amount_withdrawal = forms.FloatField(label='Quantidade retirada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    responsible = forms.ModelChoiceField(label='Responsavel', queryset=Funcionario.objects.all(),widget=forms.Select(attrs={'class':'flat'}))
    amout_refresh = forms.CharField(label='Quantidade atualizada', widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))

    class Meta:
        model = Retira_Produto
        fields = '__all__'

class FormInsereCompraProdutos(forms.ModelForm):
    product = forms.ModelChoiceField(label='Produto', queryset=Produto.objects.all(), widget=forms.Select(attrs={'class':'flat'}))
    purchase_date_product= forms.DateField(label='Data da compra',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    value_per_unit_to_buy = forms.FloatField(label='Valor por unidade comprada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    amout_purchased = forms.FloatField(label='Quantidade comprada',widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    date_vaidate = forms.DateField(label='Data da retirada',widget=forms.DateInput(attrs={'class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))

    class Meta:
        model = Compra_Produto
        fields = '__all__'