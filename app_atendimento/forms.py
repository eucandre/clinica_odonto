from django import forms
from .models import *
from input_mask.widgets import InputMask

AGENDAMENTO=((u'Atendimento clinico', 'Atendimento clinico'),(u'Exame clinico','Exame clinico'))
EVOLUCAO = ((u'Bom', 'Bom'),
            (u'Ruim', "Ruim"),
            (u'Regular', 'Regular'),
            (u'Otimo', 'Otimo'))


class Form_relatorio_exame_odonto(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                         widget=forms.Select(attrs={'class':'form-control'}))
    professional = forms.ModelChoiceField(queryset=Profissionais.objects.all(),
                                          widget=forms.Select(attrs={'class':'form-control'}))
    tooths = forms.ModelMultipleChoiceField(queryset=Dentes.objects.all())
    faces_tooths = forms.ModelMultipleChoiceField(queryset=FacesDentes.objects.all())
    date_atendence = forms.DateField(label='Data e hora para ser atendido',widget=forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'dd/mm/yyyy HH:MM ' }))

    note = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = relatorio_exame_odonto
        fields = ('name_client', 'professional', 'tooths', 'faces_tooths', 'date_atendence', 'note')

class Form_relatorio_exame_psico(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(queryset=Profissionais.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    date_atendence = forms.DateField(label='Data e hora para ser atendido', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'dd/mm/yyyy HH:MM '}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = relatorio_exame_odonto
        fields = ('name_client', 'professional', 'date_atendence', 'note')

class Form_relatorio_exame_nutri(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(queryset=Profissionais.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    date_atendence = forms.DateField(label='Data e hora para ser atendido', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'dd/mm/yyyy HH:MM '}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


    class Meta:
        model = relatorio_exame_odonto
        fields = ('name_client', 'professional', 'date_atendence', 'note')

class FormAgendamentoPlanoOdonto(forms.ModelForm):
    name_client = forms.ModelChoiceField(label='Nome do Cliente',queryset=Contrato_odonto.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    atendence = forms.ChoiceField(label='Tipo de atendimento',choices=AGENDAMENTO,widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(queryset=Profissionais.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    date_atendence = forms.DateTimeField(label='Data e hora para ser atendido',widget=forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'dd/mm/yyyy HH:MM ' }))
    note = forms.CharField(label='Observacao',widget=forms.Textarea(attrs={'class': 'form-control'}))
    active = forms.BooleanField(label='Ativo ?',widget=forms.CheckboxInput(attrs={'class': 'flat'}))

    class Meta:
        model = agendamemto_plano_odonto
        fields = ('name_client','atendence','professional','date_atendence','active','note')

class FormAgendamentoPlanoNutri(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))

    atendence = forms.ChoiceField(choices=AGENDAMENTO, widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(queryset=Profissionais.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))

    date_atendence = forms.DateField(label='Data atendiemnto',widget=forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'dd/mm/yyyy HH:MM ' }))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}))


    class Meta:
        model = agendamemto_plano_nutri
        fields = ('name_client', 'atendence', 'professional', 'date_atendence', 'active', 'note')

class FormAgendamentoPlanoPsico(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Cliente.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))

    atendence = forms.ChoiceField(choices=AGENDAMENTO, widget=forms.Select(attrs={'class': 'form-control'}))
    professional = forms.ModelChoiceField(queryset=Profissionais.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))

    date_atendence = forms.DateField(label='Data atendiemento',widget=forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'dd/mm/yyyy HH:MM ' }))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}))


    class Meta:
        model = agendamemto_plano_psico
        fields = ('name_client', 'atendence', 'professional', 'date_atendence', 'active', 'note')

class FormRelatorioExamePlanoOdonto(forms.ModelForm):

    name_client = forms.ModelChoiceField(queryset=Contrato_odonto.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    tooths = forms.ModelMultipleChoiceField(queryset=Dentes.objects.all())
    faces_tooths = forms.ModelMultipleChoiceField(queryset=FacesDentes.objects.all())
    evolution = forms.ChoiceField(choices=EVOLUCAO)
    date_atendence= forms.DateField(label='Data atendimento',widget=forms.DateInput(attrs={'type':'date','class':'form-control', 'placeholder':'dd/mm/yyyy HH:MM ' }))
    image_register = forms.FileField()
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = relatorio_exame_odonto_continuado
        fields = ('name_client','tooths','faces_tooths','evulution','date_atendence','image_register','note')

class FormRelatorioExamePlanoNutri(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Contrato_nutricionista.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    evolution = forms.ChoiceField(choices=EVOLUCAO)
    date_atendence = forms.DateField()
    image_register = forms.FileField()
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = relatorio_exame_nutri_continuado
        fields = ('name_client', 'evulution', 'date_atendence', 'note')


class FormRelatorioExamePlanoPsico(forms.ModelForm):
    name_client = forms.ModelChoiceField(queryset=Contrato_psicologo.objects.all(),
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    evolution = forms.ChoiceField(choices=EVOLUCAO)
    date_atendence = forms.DateField()
    image_register = forms.FileField()
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = relatorio_exame_psico_continuado
        fields = ('name_client', 'evulution', 'date_atendence', 'note')
