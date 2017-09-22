# coding=utf-8
from django import forms

from .models import *
from app_base.models import *

class FormCampanha(forms.ModelForm):

    name = forms.CharField(label='Nome da campanha',max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))
    date_end = forms.CharField(label='Data para o fim da campanha',max_length=150, widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    reward = forms.CharField(initial=0,label='Recompensa',max_length=150, widget=forms.TextInput(attrs={'type':'number','class':'form-control'}))
    reward1 = forms.CharField(initial=0,label='Recompensa 1',max_length=150, widget=forms.TextInput(attrs={'type':'number','class':'form-control'}))
    reward2 = forms.CharField(initial=0,label='Recompensa 2',max_length=150, widget=forms.TextInput(attrs={'type':'number','class':'form-control'}))
    reward3 = forms.CharField(initial=0,label='Recompensa 3',max_length=150, widget=forms.TextInput(attrs={'type':'number','class':'form-control'}))
    active = forms.BooleanField(required=False,label='Ativo na clinica ?',widget=forms.CheckboxInput(attrs={'class':'flat'}))
    note = forms.CharField(label='Observação',widget=forms.Textarea(attrs={"class":"form-control"}))

    class Meta:
        model = campanha
        fields = ('name', 'date_end', 'reward', 'reward1','reward2','reward3','active','note')

class FormCampanhaVenda(forms.ModelForm):
    campanha = forms.ModelChoiceField(label='Campanha',queryset=campanha.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    name_seller = forms.ModelChoiceField(label='Vendedor(a)',queryset=Funcionario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    name_client = forms.ModelChoiceField(label='Cliente',queryset=Cliente.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    value_sell = forms.IntegerField(label='Valor vendido',widget=forms.NumberInput(attrs={'class': 'form-control'}))
    note = forms.CharField(label='Observacao',max_length=100,widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = campanha_venda
        fields = ('campanha', 'name_seller', 'name_client', 'value_sell', 'note')