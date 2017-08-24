# coding=utf-8
from django import forms
from app_base.models import *
TYPE_PROFESSIONAL = ((u'Dentista', 'Dentista'), (u'Nutricionista', 'Nutricionista'), (u'Psicologo', 'Psicologo'))
SEXO = ((u'Masculino','Masculino'),(u'Feminino','Feminino'))

class FormInsereProfissionais(forms.ModelForm):

    name =  forms.CharField(label='Nome',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    professional_as = forms.ChoiceField(choices=TYPE_PROFESSIONAL, widget=forms.RadioSelect(attrs={'class':'flat'}))
    salary = forms.FloatField(label='Salário',
                              widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    sex =   forms.ChoiceField(label='Sexo',choices=SEXO,widget=forms.RadioSelect(attrs={'class':'flat'}))
    cep =   forms.CharField(label='CEP',max_length=7, widget=forms.TextInput(attrs={'class':'form-control','id':'inputSuccess5'}))
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'type':'email','class':'form-control'}))
    phone = forms.CharField(label='Telefone',max_length=10, widget=forms.TextInput(attrs={'class':'form-control','id':'inputSuccess5'}))
    register = forms.CharField(label='Rregistro',max_length=150, widget=forms.TextInput(attrs={'class':'form-control','id':'inputSuccess5'}))
    birth_day = forms.DateField(label='Data de nascimento',widget=forms.DateInput(attrs={'type':'date','class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    note = forms.CharField(label='Observação',widget=forms.Textarea(attrs={"class":"form-control"}))
    active = forms.BooleanField(label='Ativo na clínica?',widget=forms.CheckboxInput(attrs={'class':'flat'}))

    class Meta:
        model = Profissionais
        fields = ('name', 'professional_as', 'salary','sex', 'cep', 'email', 'phone', 'register', 'birth_day', 'note', 'active')

class FormInsereFuncionario(forms.ModelForm):
    name =  forms.CharField(label='Nome',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    date_entry = forms.DateField(label='Data de entrada',widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    sex =   forms.ChoiceField(label='Sexo',choices=SEXO,widget=forms.RadioSelect(attrs={'class':'flat'}))
    function = forms.ChoiceField(label='Função',choices = FUNCTION,widget=forms.RadioSelect(attrs={'class':'flat'}))
    email = forms.EmailField(label='E-mail',help_text='email@email.com',widget=forms.EmailInput(attrs={'type':'email','class':'form-control'}))
    phone = forms.CharField(label='Telefone',max_length=10, widget=forms.TextInput(attrs={'type':'phone','class':'form-control','id':'inputSuccess5'}))
    street = forms.CharField(label='Rua',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    district = forms.CharField(label='Bairro',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    city = forms.CharField(label='Cidade',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    rg = forms.CharField(max_length=25,  widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    cpf = forms.CharField(max_length=11,  widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    birth_day = forms.DateField(label='Data de nascimento',widget=forms.DateInput(attrs={'type':'date','class':'form-control', "data-inputmask":"'mask': '99/99/9999'"}))
    note = forms.CharField(label='Observação',widget=forms.Textarea(attrs={"class":"form-control"}))
    salary = forms.FloatField(label='Salário',widget=forms.TextInput(attrs={'type':'number','class':'form-control col-md-7 col-xs-12'}))
    active = forms.BooleanField(label='Ativo na clínica?',widget=forms.CheckboxInput(attrs={'class':'flat'}))

    class Meta:
        model = Funcionario
        fields = ('name','date_entry','sex','function','email','phone','street','district','city','rg','cpf','cep','birth_day','note','salary','active')

class FormInsereCliente(forms.ModelForm):
    name = forms.CharField(label='Nome',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    sex = forms.ChoiceField(label='Sexo',choices=SEXO,widget=forms.RadioSelect(attrs={'class':'flat'}))
    date_register = forms.DateField(label='Data de registro',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    profession = forms.CharField(label='Profissão', max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    phone = forms.CharField(label='Telefone',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class':'form-control','id':'inputSuccess5'}))
    rg = forms.CharField(max_length=25,  widget=forms.TextInput(attrs={'class':'form-control','id':'inputSuccess5'}))
    cpf = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class':'form-control','id':'inputSuccess5'}))
    birth_day = forms.DateField(label='Data de Nascimento',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    street = forms.CharField(label='Rua',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    district = forms.CharField(label='Bairro',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    city = forms.CharField(label='Cidade',max_length=150, widget=forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12'}))
    Note = forms.CharField(label='Observação',widget=forms.Textarea(attrs={"class":"form-control"}))
    active = forms.BooleanField(label='Cliente ativo?',widget=forms.CheckboxInput(attrs={'class':'flat'}))

    class Meta:
        model = Cliente
        fields = ('name','sex','date_register','profession','email','phone','cep','cpf','rg','birth_day','street','district','city','Note','active')

class FormInsereContatoCliente(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    sex = forms.ChoiceField(label='Sexo', choices=SEXO, widget=forms.RadioSelect(attrs={'class': 'flat'}))
    phone = forms.CharField(label='Telefone', max_length=150,
                            widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    city = forms.CharField(label='Cidade', max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    profession = forms.CharField(label='Profissao', max_length=150,
                                 widget=forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}))
    cliente = forms.BooleanField(label='Cliente ?', widget=forms.CheckboxInput(attrs={'class': 'flat'}))
    indicado_por = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Cotatos_Clientes_indicacoes
        fields = ('name','sex','phone','email','city','profession','cliente','indicado_por')