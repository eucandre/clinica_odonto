
from datetime import date
from django.core.paginator import *
from django.http import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required(login_url='/login/')
def lista_relatorios_exame_odonto(request):
    lista_relatorios_exame_odonto = relatorio_exame_odonto.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_relatorios_exame_odonto, 10)
    try:
        p_relatorio_exame_odonto = paginator.page(page)
    except PageNotAnInteger:
        p_relatorio_exame_odonto = paginator.page(1)
    except EmptyPage:
        p_relatorio_exame_odonto = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_relatorio_exame_odonto.html', {'p_relatorio_exame_odonto': p_relatorio_exame_odonto})

@login_required(login_url='/login/')
def insere_relatorio_exame_odonto(request):
    if request.method =='POST':
        form = Form_relatorio_exame_odonto(request.POST)
        if form.is_valid():
            item = form.save(commit= False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = Form_relatorio_exame_odonto()
    return render(request,'pagina_app_atendimento/insere_relatorio_exame_odonto.html', {'form':form})

@login_required(login_url='/login/')
def edita_relatorio_exame_odonto(request, nr_item):
    item = relatorio_exame_odonto.objects.get(pk=nr_item)
    if request.method =='POST':
        form = Form_relatorio_exame_odonto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = Form_relatorio_exame_odonto(instance=item)
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_odonto.html', {'form': form})

@login_required(login_url='/login/')
def detalha_relatorio_exame_odonto(request, nr_item):
    try:
        item = relatorio_exame_odonto.objects.get(pk=nr_item)
    except relatorio_exame_odonto.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_relatorio_exame_odonto.html", {'item': item})

@login_required(login_url='/login/')
def lista_relatorios_exame_psico(request):
    lista_relatorios_exame_psico = relatorio_exame_psico.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_relatorios_exame_psico, 10)
    try:
        p_relatorio_exame_psico = paginator.page(page)
    except PageNotAnInteger:
        p_relatorio_exame_psico = paginator.page(1)
    except EmptyPage:
        p_relatorio_exame_psico = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_relatorio_exame_psico.html', {'p_relatorio_exame_psico': p_relatorio_exame_psico})

@login_required(login_url='/login/')
def insere_relatorio_exame_psico(request):
    if request.method =='POST':
        form = Form_relatorio_exame_psico(request.POST)
        if form.is_valid():
            item = form.save(commit= False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = Form_relatorio_exame_psico()
    return render(request,'pagina_app_atendimento/isere_relatorio_exame_psico.html', {'form':form})

@login_required(login_url='/login/')
def edita_relatorio_exame_psico(request, nr_item):
    item = relatorio_exame_psico.objects.get(pk=nr_item)
    if request.method =='POST':
        form = Form_relatorio_exame_psico(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = Form_relatorio_exame_psico(instance=item)
        return render(request, 'pagina_app_atendimento/isere_relatorio_exame_psico.html', {'form': form})

@login_required(login_url='/login/')
def detalha_relatorio_exame_psico(request, nr_item):
    try:
        item = relatorio_exame_psico.objects.get(pk=nr_item)
    except relatorio_exame_psico.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_relatorio_exame_psico.html", {'item': item})

@login_required(login_url='/login/')
def lista_relatorios_exame_nutri(request):
    lista_relatorios_exame_nutri = relatorio_exame_nutri.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_relatorios_exame_nutri, 10)
    try:
        p_relatorio_exame_nutri = paginator.page(page)
    except PageNotAnInteger:
        p_relatorio_exame_nutri = paginator.page(1)
    except EmptyPage:
        p_relatorio_exame_nutri = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_relatorio_exame_nutri.html', {'p_relatorio_exame_nutri': p_relatorio_exame_nutri})

@login_required(login_url='/login/')
def insere_relatorio_exame_nutri(request):
    if request.method =='POST':
        form = Form_relatorio_exame_nutri(request.POST)
        if form.is_valid():
            item = form.save(commit= False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = Form_relatorio_exame_nutri()
    return render(request,'pagina_app_atendimento/isere_relatorio_exame_nutri.html', {'form':form})

@login_required(login_url='/login/')
def edita_relatorio_exame_nutri(request, nr_item):
    item = relatorio_exame_nutri.objects.get(pk=nr_item)
    if request.method =='POST':
        form = Form_relatorio_exame_nutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = Form_relatorio_exame_nutri(instance=item)
        return render(request, 'pagina_app_atendimento/isere_relatorio_exame_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_relatorio_exame_nutri(request, nr_item):
    try:
        item = relatorio_exame_nutri.objects.get(pk=nr_item)
    except relatorio_exame_nutri.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_relatorio_exame_nutri.html", {'item': item})

@login_required(login_url='/login/')
def insere_agendamento_plano_odonto(request):
    if request.method == 'POST':
        form = FormAgendamentoPlanoOdonto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormAgendamentoPlanoOdonto()
        return render(request, 'pagina_app_atendimento/insere_agendamento_plano_odonto.html', {'form': form})

@login_required(login_url='/login/')
def lista_agendamento_plano_odonto(request):
    lista_agendamento_plano_odonto = agendamemto_plano_odonto.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_agendamento_plano_odonto, 10)
    try:
        p_agendamento = paginator.page(page)
    except PageNotAnInteger:
        p_agendamento = paginator.page(1)
    except EmptyPage:
        p_agendamento = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_agendamento_plano_odonto.html', {'p_agendamento': p_agendamento})

@login_required(login_url='/login/')
def edita_agendamento_plano_odonto(request, nr_item):
    item = agendamemto_plano_odonto.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormAgendamentoPlanoOdonto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormAgendamentoPlanoOdonto(instance=item)
        return render(request, 'pagina_app_atendimento/isere_relatorio_exame_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_agendamento_plano_odonto(request, nr_item):
    try:
        item = agendamemto_plano_odonto.objects.get(pk=nr_item)
    except agendamemto_plano_odonto.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_agendamento_plano_odonto.html", {'item': item})

@login_required(login_url='/login/')
def insere_agendamento_plano_nutri(request):
    if request.method == 'POST':
        form = FormAgendamentoPlanoOdonto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormAgendamentoPlanoOdonto()
        return render(request, 'pagina_app_atendimento/insere_agendamento_plano_nutri.html', {'form': form})

@login_required(login_url='/login/')
def lista_agendamento_plano_nutri(request):
    lista_agendamento_plano_nutri = agendamemto_plano_nutri.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_agendamento_plano_nutri, 10)
    try:
        p_agendamento = paginator.page(page)
    except PageNotAnInteger:
        p_agendamento = paginator.page(1)
    except EmptyPage:
        p_agendamento = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_agendamento_plano_nutri.html', {'p_agendamento': p_agendamento})

@login_required(login_url='/login/')
def edita_agendamento_plano_nutri(request, nr_item):
    item = agendamemto_plano_nutri.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormAgendamentoPlanoNutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormAgendamentoPlanoNutri(instance=item)
        return render(request, 'pagina_app_atendimento/isere_relatorio_exame_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_agendamento_plano_nutri(request, nr_item):
    try:
        item = agendamemto_plano_nutri.objects.get(pk=nr_item)
    except agendamemto_plano_nutri.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_agendamento_plano_nutri.html", {'item': item})

@login_required(login_url='/login/')
def insere_agendamento_plano_psico(request):
    if request.method == 'POST':
        form = FormAgendamentoPlanoOdonto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormAgendamentoPlanoOdonto()
        return render(request, 'pagina_app_atendimento/insere_agendamento_plano_psico.html', {'form': form})

@login_required(login_url='/login/')
def lista_agendamento_plano_psico(request):
    lista_agendamento_plano_psico = agendamemto_plano_psico.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_agendamento_plano_psico, 10)
    try:
        p_agendamento = paginator.page(page)
    except PageNotAnInteger:
        p_agendamento = paginator.page(1)
    except EmptyPage:
        p_agendamento = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_agendamento_plano_psico.html', {'p_agendamento': p_agendamento})

@login_required(login_url='/login/')
def edita_agendamento_plano_psico(request, nr_item):
    item = agendamemto_plano_psico.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormAgendamentoPlanoNutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormAgendamentoPlanoNutri(instance=item)
        return render(request, 'pagina_app_atendimento/isere_relatorio_exame_psico.html', {'form': form})

@login_required(login_url='/login/')
def detalha_agendamento_plano_psico(request, nr_item):
    try:
        item = agendamemto_plano_psico.objects.get(pk=nr_item)
    except agendamemto_plano_psico.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_agendamento_plano_psico.html", {'item': item})

@login_required(login_url='/login/')
def mapa_atendimento_odonto(request):

    '''
        Este metodo tem a tarefa de compilar todos os atendiemntos agendados diariamente
    '''
    data_de_hoje = date.today()
    data_de_amanha = date.fromordinal(data_de_hoje.toordinal()+1)
    atendiementos_odonto = agendamemto_plano_odonto.objects.all().filter(date_atendence=data_de_hoje)
    #atendiementos_psico = agendamemto_plano_psico.objects.all().filter(date_atendence=data_de_hoje)
   # atendiementos_nutri = agendamemto_plano_nutri.objects.all().filter(date_atendence=data_de_hoje)
    atendimentos_odonto_amanha = agendamemto_plano_odonto.objects.all().filter(date_atendence=data_de_amanha)
    #atendimentos_nutri_amanha = agendamemto_plano_nutri.objects.all().filter(date_atendence=data_de_amanha)
   # atendimentos_psico_amanha = agendamemto_plano_psico.objects.all().filter(date_atendence=data_de_amanha)
    #atendimentos_odonto= atendiementos_odonto#, atendiementos_nutri, atendiementos_psico
    atende_amanha= atendimentos_odonto_amanha#,atendimentos_psico_amanha,atendimentos_nutri_amanha
    return render(request,'mapa_atendiemnto.html',{'agenda_odonto':atendiementos_odonto, 'agenda_odonto_amanha':atende_amanha})

@login_required(login_url='/login/')
def insere_relatorio_exame_plano_odonto(request):
    if request.method == 'POST':
        form = FormRelatorioExamePlanoOdonto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRelatorioExamePlanoOdonto()
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_plano_odonto.html', {'form': form})

@login_required(login_url='/login/')
def lista_relatorio_exame_plano_odonto(request):
    lista_exame_plano_odonto_continuado = relatorio_exame_odonto_continuado.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_exame_plano_odonto_continuado, 10)
    try:
        p_relatorio_exame_odonto = paginator.page(page)
    except PageNotAnInteger:
        p_relatorio_exame_odonto = paginator.page(1)
    except EmptyPage:
        p_relatorio_exame_odonto = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_exame_plano_odonto_continuado.html', {'p_agendamento': p_relatorio_exame_odonto})

@login_required(login_url='/login/')
def edita_realtorio_exame_odonto_continuado(request, nr_item):
    item = relatorio_exame_odonto_continuado.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRelatorioExamePlanoOdonto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRelatorioExamePlanoOdonto(instance=item)
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_plano_odonto.html', {'form': form})

@login_required(login_url='/login/')
def detalha_relatorio_exame_odonto_continuado(request, nr_item):
    try:
        item = relatorio_exame_odonto_continuado.objects.get(pk=nr_item)
    except relatorio_exame_odonto_continuado.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_relatorio_exame_plano_odonto.html", {'item': item})


@login_required(login_url='/login/')
def insere_relatorio_exame_plano_nutri(request):
    if request.method == 'POST':
        form = FormRelatorioExamePlanoNutri(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRelatorioExamePlanoNutri()
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_plano_nutri.html', {'form': form})

@login_required(login_url='/login/')
def lista_relatorio_exame_plano_nutri(request):
    lista_exame_plano_nutri_continuado = relatorio_exame_nutri_continuado.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_exame_plano_nutri_continuado, 10)
    try:
        p_relatorio_exame_plano_nutri = paginator.page(page)
    except PageNotAnInteger:
        p_relatorio_exame_plano_nutri = paginator.page(1)
    except EmptyPage:
        p_relatorio_exame_plano_nutri = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_exame_plano_nutri_continuado.html', {'p_agendamento': p_relatorio_exame_plano_nutri})

@login_required(login_url='/login/')
def edita_realtorio_exame_nutri_continuado(request, nr_item):
    item = relatorio_exame_nutri_continuado.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRelatorioExamePlanoNutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRelatorioExamePlanoNutri(instance=item)
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_plano_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_relatorio_exame_nutri_continuado(request, nr_item):
    try:
        item = relatorio_exame_nutri_continuado.objects.get(pk=nr_item)
    except relatorio_exame_nutri_continuado.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_relatorio_exame_plano_odonto.html", {'item': item})

@login_required(login_url='/login/')
def insere_relatorio_exame_plano_psico(request):
    if request.method == 'POST':
        form = FormRelatorioExamePlanoPsico(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRelatorioExamePlanoPsico()
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_plano_psico.html', {'form': form})

@login_required(login_url='/login/')
def lista_relatorio_exame_plano_psico(request):
    lista_exame_plano_psico_continuado = relatorio_exame_psico_continuado.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(lista_exame_plano_psico_continuado, 10)
    try:
        p_relatorio_exame_plano_psico = paginator.page(page)
    except PageNotAnInteger:
        p_relatorio_exame_plano_psico = paginator.page(1)
    except EmptyPage:
        p_relatorio_exame_plano_psico = paginator.page(paginator.num_pages)
    return render(request, 'pagina_app_atendimento/lista_exame_plano_psico_continuado.html', {'p_agendamento': p_relatorio_exame_plano_psico})

@login_required(login_url='/login/')
def edita_realtorio_exame_psico_continuado(request, nr_item):
    item = relatorio_exame_psico_continuado.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRelatorioExamePlanoPsico(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRelatorioExamePlanoPsico(instance=item)
        return render(request, 'pagina_app_atendimento/insere_relatorio_exame_plano_psico.html', {'form': form})

@login_required(login_url='/login/')
def detalha_relatorio_exame_psico_continuado(request, nr_item):
    try:
        item = relatorio_exame_psico_continuado.objects.get(pk=nr_item)
    except relatorio_exame_psico_continuado.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "pagina_app_atendimento/item_relatorio_exame_plano_psico.html", {'item': item})

