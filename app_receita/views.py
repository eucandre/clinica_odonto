from django.shortcuts import render
from app_receita.forms import *
from django.http import *
from django.core.paginator import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from app_receita.verifica_pagamento import *
@login_required(login_url='/login/')
def lista_dentes(request):
    try:
        dentes = Dentes.objects.all()
        return render(request, "paginas_app_receita/lista_dentes.html", {"dentes": dentes})
    except Dentes.DoesNotExist:
        raise Http404('Sem Registros!')

@login_required(login_url='/login/')
def edita_dentes(request, nr_item):
    item = Dentes.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormDentes(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormDentes(instance=item)
    return render(request, 'paginas_app_receita/insere_dentes.html', {'form': form})

@login_required(login_url='/login/')
def detalha_dentes(request, nr_item):
    try:
        item = Dentes.objects.get(pk=nr_item)
    except Dentes.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_dentes.html", {'item': item})

@login_required(login_url='/login/')
def InsereDentes(request):

    if not request.user.has_perm('app_receita.add_dentes'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = FormDentes(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormDentes()
    return render(request, 'paginas_app_receita/insere_dentes.html', {'form':form})

@login_required(login_url='/login/')
def lista_orcamentoOdonto(request):
    orcamento_odonto = OrcamentoPlanoOdontologico.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(orcamento_odonto, 10)
    try:
        p_orcamento = paginator.page(page)
    except PageNotAnInteger:
        p_orcamento = paginator.page(1)
    except EmptyPage:
        p_orcamento = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_orcamento_odonto.html", {"orcamentos": p_orcamento})

@login_required(login_url='/login/')
def edita_orcamentoodonto(request, nr_item):
    item = OrcamentoPlanoOdontologico.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormOrcamentoOdontologico(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormOrcamentoOdontologico(instance=item)
    return render(request, 'paginas_app_receita/insere_dentes.html', {'form': form})

@login_required(login_url='/login/')
def detalha_orcamentoodonto(request, nr_item):
    try:
        item = OrcamentoPlanoOdontologico.objects.get(pk=nr_item)
    except OrcamentoPlanoOdontologico.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_orcamentoodonto.html", {'item': item})

@login_required(login_url='/login/')
def InsereOrcamentoOdonto(request):
    if request.method == 'POST':
        form = FormOrcamentoOdontologico(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormOrcamentoOdontologico()
    return render(request, 'paginas_app_receita/insere_orcamento_odonto.html', {'form':form})

@login_required(login_url='/login/')
def lista_orcamentonutri(request):
    orcamento_nutri = OrcamentoPlanoNutri.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(orcamento_nutri, 10)
    try:
        orcanto_nutri = paginator.page(page)
    except PageNotAnInteger:
        orcanto_nutri = paginator.page(1)
    except EmptyPage:
        orcanto_nutri = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_orcamentonutri.html", {"orcamento_nutri": orcanto_nutri})

@login_required(login_url='/login/')
def InsereOrcamentoNutri(request):
    if request.method == 'POST':
        form = FormOrcamentoPlanoNutri(request.POST)
        if form.is_valid():
            item = form.save(commit = False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormOrcamentoPlanoNutri()
    return render(request, 'paginas_app_receita/insere_orcamento_nutri.html', {'form':form})

@login_required(login_url='/login/')
def edita_orcamento_nutri(request, nr_item):
    item = OrcamentoPlanoNutri.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormOrcamentoPlanoNutri(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormOrcamentoPlanoNutri(instance=item)
    return render(request, 'paginas_app_receita/insere_orcamento_nutri.html', {'form': form})

@login_required(login_url='/login/')
def detalha_orcamento_nutri(request, nr_item):
    try:
        item = OrcamentoPlanoNutri.objects.get(pk=nr_item)
    except OrcamentoPlanoNutri.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_orcamento_nutri.html", {'item': item})

@login_required(login_url='/login/')
def lista_orcamento_psico(request):
    orcamento_psico = OrcamentoPlanoPsico.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(orcamento_psico, 10)
    try:
        p_orcamento_psico = paginator.page(page)
    except PageNotAnInteger:
        p_orcamento_psico = paginator.page(1)
    except EmptyPage:
        p_orcamento_psico = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_orcamento_psico.html", {"orcamentos": p_orcamento_psico})

@login_required(login_url='/login/')
def edita_orcamento_psico(request, nr_item):
    item = OrcamentoPlanoPsico.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormOrcamentoPlanoPsico(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormOrcamentoPlanoPsico(instance=item)
    return render(request, 'paginas_app_receita/insere_orcamento_psico.html', {'form': form})

@login_required(login_url='/login/')
def InsereOrcamentoPsico(request):
    if request.method == 'POST':
        form = FormOrcamentoPlanoPsico(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormOrcamentoPlanoPsico()
    return render(request, 'paginas_app_receita/insere_orcamento_psico.html', {'form': form})

@login_required(login_url='/login/')
def detalha_orcamento_psico(request, nr_item):
    try:
        item = OrcamentoPlanoPsico.objects.get(pk=nr_item)
    except OrcamentoPlanoPsico.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_orcamento_psico.html", {'item': item})

@login_required(login_url='/login/')
def lista_atendimento_avulso(request):
    orcamento_avulso = RecebimentoAvulso.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(orcamento_avulso, 10)
    try:
        p_atendimento_avulso = paginator.page(page)
    except PageNotAnInteger:
        p_atendimento_avulso = paginator.page(1)
    except EmptyPage:
        p_atendimento_avulso = paginator.page(paginator.num_pages)
    return render(request, "paginas_app_receita/lista_atendimento_avulso.html", {"orcamentos": p_atendimento_avulso})

@login_required(login_url='/login/')
def detalha_atendimento_avulso(request, nr_item):
    try:
        item = RecebimentoAvulso.objects.get(pk=nr_item)
    except RecebimentoAvulso.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_atendimento_avulso.html", {'item': item})

@login_required(login_url='/login/')
def edita_atendiemento_avulso(request,nr_item):
    item = RecebimentoAvulso.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormRecebimentoAvulso(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormRecebimentoAvulso(instance=item)
    return render(request, 'paginas_app_receita/insere_atendimento_avulso.html', {'form': form})

@login_required(login_url='/login/')
def InsereAtendimentoAvulso(request):
    if request.method == 'POST':
        form = FormRecebimentoAvulso(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormRecebimentoAvulso()
    return render(request, 'paginas_app_receita/insere_atendimento_avulso.html', {'form': form})

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
    recebimento_plano = RecebimentoPlano.objects.all()
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

    item = RecebimentoPlano.objects.get(pk=nr_item)
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
        item = RecebimentoPlano.objects.get(pk=nr_item)
    except RecebimentoPlano.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_receita/item_recebimento_plano.html", {'item': item , 'situacao':VerificaPagamento(nr_item)})
