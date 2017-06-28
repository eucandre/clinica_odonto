from django.http import *
from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.core.paginator import *
from app_receita.verifica_pagamento import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def InsereContratoOdonto(request):
    if request.method == 'POST':
        form = FormContratoOdonto(request.POST)
        if form.is_valid():
            item =  form.save(commit=False)
            item.user = request.user
            item.save()
            messages.info(request, 'Salvo com sucesso!')
            return render(request,'salvo.html',{})

    else:
        form = FormContratoOdonto()
    return render(request, 'paginas_app_contrato/insere_contrato_odonto.html', {'form':form})

@login_required(login_url='/login/')
def lista_ContratoOdonto(request):

    lista_contrato_odonto = Contrato_odonto.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(lista_contrato_odonto, 10)

    try:
        p_contrato_odonto = paginator.page(page)
    except PageNotAnInteger:
        p_contrato_odonto = paginator.page(1)
    except EmptyPage:
        p_contrato_odonto = paginator.page(paginator.num_pages)
    return render(request,'paginas_app_contrato/lista_contrato_odonto.html', {'contratos':p_contrato_odonto})

@login_required(login_url='/login/')
def edita_contrato_odonto(request, nr_item):
    item = Contrato_odonto.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormContratoOdonto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormContratoOdonto(instance=item)
    return render(request, 'paginas_app_contrato/insere_contrato_odonto.html', {'form': form})

@login_required(login_url='/login/')
def detalha_contrato_odonto(request, nr_item):
    try:
        item = Contrato_odonto.objects.get(pk=nr_item)
    except Contrato_odonto.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_contrato/item_contrato_odonto.html", {'item': item})

@login_required(login_url='/login/')
def InsereContratoNutri(request):
    if request.method == 'POST':
        form = FormContratoNutri(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.info(request, 'Salvo com sucesso!')
    else:
        form = FormContratoNutri()
    return render(request, 'paginas_app_contrato/insere_contrato_nutri.html', {'form': form})

@login_required(login_url='/login/')
def InsereContratoPsico(request):
    if request.method == 'POST':
        form = FormContratoPsico(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.info(request, 'Salvo com sucesso!')
    else:
        form = FormContratoPsico()
    return render(request, 'paginas_app_contrato/insere_contrato_psico.html', {'form': form})