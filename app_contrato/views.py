from django.http import *
from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.core.paginator import *
from app_receita.verifica_pagamento import *
from django.contrib.auth.decorators import login_required
from app_base.views import *

@login_required(login_url='/login/')
def InsereContratoOdonto(request):
    if request.method == 'POST':
        form = FormContratoOdonto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
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
    obj_r = RecebimentoPlanoOdonto.objects.get(pk=item.propose.name_client.id)
    if request.method == 'POST':
        form = FormContratoOdonto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormContratoOdonto(instance=item)
    return render(request, 'paginas_app_contrato/insere_contrato_odonto.html', {'form': form, 'cortesia':obj_r})# 'valor_pago':itemr.TotalPagoTratamento})

@login_required(login_url='/login/')
def detalha_contrato_odonto(request, nr_item):
    try:
        item = Contrato_odonto.objects.get(pk=nr_item)
        obj_r = RecebimentoPlanoOdonto.objects.get(pk=item.propose.name_client.id)
        proposta = Orcamento_Plano_Odonto.objects.get(pk=item.id)
    except Contrato_odonto.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_contrato/item_contrato_odonto.html", {'item': item,'valor_pago':obj_r,'proposta':proposta})


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
def lista_ContratoNutri(request):

    lista_contrato_nutri = Contrato_nutricionista.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(lista_contrato_nutri, 10)

    try:
        p_contrato_odonto = paginator.page(page)
    except PageNotAnInteger:
        p_contrato_odonto = paginator.page(1)
    except EmptyPage:
        p_contrato_odonto = paginator.page(paginator.num_pages)
    return render(request,'paginas_app_contrato/lista_contrato_nutri.html', {'contratos':p_contrato_odonto})

@login_required(login_url='/login/')
def edita_contrato_nutri(request, nr_item):
    item = Contrato_nutricionista.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormContratoNutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormContratoNutri(instance=item)
    return render(request, 'paginas_app_contrato/insere_contrato_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_contrato_nutri(request, nr_item):
    try:
        item = Contrato_nutricionista.objects.get(pk=nr_item)
    except Contrato_nutricionista.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_contrato/item_contrato_nutri.html", {'item': item})


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

@login_required(login_url='/login/')
def lista_ContratoPsico(request):

    lista_contrato_pscico = Contrato_psicologo.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(lista_contrato_pscico, 10)

    try:
        p_contrato_odonto = paginator.page(page)
    except PageNotAnInteger:
        p_contrato_odonto = paginator.page(1)
    except EmptyPage:
        p_contrato_odonto = paginator.page(paginator.num_pages)
    return render(request,'paginas_app_contrato/lista_contrato_psico.html', {'contratos':p_contrato_odonto})

@login_required(login_url='/login/')
def edita_contrato_psico(request, nr_item):
    item = Contrato_psicologo.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormContratoPsico(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormContratoPsico(instance=item)
    return render(request, 'paginas_app_contrato/insere_contrato_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_contrato_psico(request, nr_item):
    try:
        item = Contrato_psicologo.objects.get(pk=nr_item)
    except Contrato_psicologo.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_contrato/item_contrato_psico.html", {'item': item})

@login_required(login_url='/login/')
def InsereRecebimentoPlano(request):
    if request.method == 'POST':
        form = FormRecebimentoPlano(request.POST)
        if form.is_valid():
            item =  form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormRecebimentoPlano()
    return render(request, 'paginas_app_receita/insere_recebimento_plano.html', {'form': form})

@login_required(login_url='/login/')
def lista_recebimento_plano(request):
    recebimento_plano = RecebimentoPlanoOdonto.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(recebimento_plano, 10)
    try:
        p_recebimento_plano = paginator.page(page)
    except PageNotAnInteger:
        p_recebimento_plano = paginator.page(1)
    except EmptyPage:
        p_recebimento_plano = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_recebimento_plano.html", {"recebimento_plano": p_recebimento_plano})

@login_required(login_url='/login/')
def edita_recebimento_plano(request, nr_item):

    item = RecebimentoPlanoOdonto.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRecebimentoPlano(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRecebimentoPlano(instance=item)
    return render(request, 'paginas_app_receita/insere_recebimento_plano.html', {'form': form})

@login_required(login_url='/login/')
def detalha_recebimento_plano(request, nr_item):
    try:
        item = RecebimentoPlanoOdonto.objects.get(pk=nr_item)
    except RecebimentoPlanoOdonto.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_recebimento_plano.html", {'item': item , 'situacao':VerificaPagamento(nr_item)})

@login_required(login_url='/login/')
def lista_recebimento_plano_nutri(request):
    recebimento_plano = RecebimentoPlanoNutri.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(recebimento_plano, 10)
    try:
        p_recebimento_plano = paginator.page(page)
    except PageNotAnInteger:
        p_recebimento_plano = paginator.page(1)
    except EmptyPage:
        p_recebimento_plano = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_recebimento_plano_nutri.html", {"recebimento_plano": p_recebimento_plano})

@login_required(login_url='/login/')
def edita_recebimento_plano_nutri(request, nr_item):

    item = RecebimentoPlanoNutri.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRecebimentoPlanoNutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRecebimentoPlanoNutri(instance=item)
    return render(request, 'paginas_app_receita/insere_recebimento_plano_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_recebimento_plano_nutri(request, nr_item):
    try:
        item = RecebimentoPlanoNutri.objects.get(pk=nr_item)
    except RecebimentoPlanoNutri.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_recebimento_plano_nutri.html", {'item': item , 'situacao':VerificaPagamento(nr_item)})

@login_required(login_url='/login/')
def InsereRecebimentoPlanoNutri(request):
    if request.method == 'POST':
        form = FormRecebimentoPlanoNutri(request.POST)
        if form.is_valid():
            item =  form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormRecebimentoPlanoNutri()
    return render(request, 'paginas_app_receita/insere_recebimento_plano_nutri.html', {'form': form})

@login_required(login_url='/login/')
def lista_recebimento_plano_Psico(request):
    recebimento_plano = RecebimentoPlanoPsico.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(recebimento_plano, 10)
    try:
        p_recebimento_plano = paginator.page(page)
    except PageNotAnInteger:
        p_recebimento_plano = paginator.page(1)
    except EmptyPage:
        p_recebimento_plano = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_recebimento_plano_Psico.html", {"recebimento_plano": p_recebimento_plano})

@login_required(login_url='/login/')
def edita_recebimento_plano_Psico(request, nr_item):

    item = RecebimentoPlanoPsico.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRecebimentoPlanoPsico(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRecebimentoPlano(instance=item)
    return render(request, 'paginas_app_receita/insere_recebimento_plano_Psico.html', {'form': form})

@login_required(login_url='/login/')
def detalha_recebimento_plano_Psico(request, nr_item):
    try:
        item = RecebimentoPlanoPsico.objects.get(pk=nr_item)
    except RecebimentoPlanoPsico.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_recebimento_plano_Psico.html", {'item': item , 'situacao':VerificaPagamento(nr_item)})

@login_required(login_url='/login/')
def InsereRecebimentoPlanoPsico(request):
    if request.method == 'POST':
        form = FormRecebimentoPlanoPsico(request.POST)
        if form.is_valid():
            item =  form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormRecebimentoPlanoPsico()
    return render(request, 'paginas_app_receita/insere_recebimento_plano_Psico.html', {'form': form})

@login_required(login_url='/login/')
def InsereContratoEmpresa(request):
    if request.method =='POST':
        form = FormContratoEmpresa(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form =FormContratoEmpresa()
    return render(request, 'paginas_app_contrato/contrato_empresa.html',{'form':form})

@login_required(login_url='/login/')
def EditaContratoEmpresa(request, nr_item):

    item = Contrato_Empresa.objects.get(pk=nr_item)
    if request.method =='POST':
        form = FormContratoEmpresa(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form =FormContratoEmpresa(instance=item)
    return render(request, 'paginas_app_contrato/contrato_empresa.html',{'form':form})

@login_required(login_url='/login/')
def detalha_Contrato_Empresa(request, nr_item):
    try:
        item = Contrato_Empresa.objects.get(pk=nr_item)
    except Contrato_Empresa.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_contrato/item_contrato_empresa.html", {'item': item })

@login_required(login_url='/login/')
def lista_contrtos_empresa(request):
    contrtos_empresa = Contrato_Empresa.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(contrtos_empresa, 10)
    try:
        p_contrtos_empresa = paginator.page(page)
    except PageNotAnInteger:
        p_contrtos_empresa = paginator.page(1)
    except EmptyPage:
        p_contrtos_empresa = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_contrato/lista_contrtos_empresa.html", {"contrtos_empresa": p_contrtos_empresa})

@login_required(login_url='/login/')
def InsereContratoFiliadosEmpresa(request):
    if request.method =='POST':
        form = FormContratoFiliadoEmpresa(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form =FormContratoFiliadoEmpresa()
    return render(request, 'paginas_app_contrato/contrato_empresa.html',{'form':form})

@login_required(login_url='/login/')
def EditaContratoFiliadoEmpresa(request, nr_item):

    item = Contrato_Filiado_A_Empresa.objects.get(pk=nr_item)
    if request.method =='POST':
        form = FormContratoFiliadoEmpresa(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form =FormContratoFiliadoEmpresa(instance=item)
    return render(request, 'paginas_app_contrato/contrato_filiado_empresa.html',{'form':form})

@login_required(login_url='/login/')
def detalha_Contrato_Filiado_Empresa(request, nr_item):
    try:
        item = Contrato_Filiado_A_Empresa.objects.get(pk=nr_item)
    except Contrato_Filiado_A_Empresa.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_contrato/item_contrato_filiado_empresa.html", {'item': item })

@login_required(login_url='/login/')
def lista_contrtos_Filiado_empresa(request):
    contrtos_filiafo_empresa = Contrato_Filiado_A_Empresa.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(contrtos_filiafo_empresa, 10)
    try:
        p_contrtos_filiafo_empresa = paginator.page(page)
    except PageNotAnInteger:
        p_contrtos_filiafo_empresa = paginator.page(1)
    except EmptyPage:
        p_contrtos_filiafo_empresa = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_contrato/lista_contrtos_filiafo_empresa.html", {"contrtos_filiafo_empresa": p_contrtos_filiafo_empresa})

