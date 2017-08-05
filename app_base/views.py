from django.shortcuts import *
from app_base.forms import *
from app_receita.models import *
from django.http import *
from django.core.paginator import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django import template
from django.contrib.auth.models import Group
from app_atendimento.models import *


@login_required(login_url='/login/')
def lista_profissionais(request):
    try:
        profissionais = Profissionais.objects.all()
        return render(request, "paginas_app_base/lista_profissionais.html", {"profissionais": profissionais})
    except Profissionais.DoesNotExist:
        raise Http404('Sem Registros!')

@login_required(login_url='/login/')
def lista_funcionarios(request):

    funcionario = Funcionario.objects.all()
    return render(request, "paginas_app_base/lista_funcionarios.html", {"funcionarios": funcionario})

@login_required(login_url='/login/')
def lista_clientes(request):
    clients = Cliente.objects.all()
    page = request.GET.get('page',1)
    paginatior = Paginator(clients, 10)
    try:
        p_clientes = paginatior.page(page)
    except PageNotAnInteger:
        p_clientes = paginatior.page(1)
    except EmptyPage:
        p_clientes = paginatior.page(paginatior.num_pages)
    return render(request, "paginas_app_base/lista_clientes.html", {"clientes": p_clientes})


@login_required(login_url='/login/')
def inicia(request):
    # variaveis gerais aqui declaradas
    clientes = Cliente.objects.all()
    contratos_odonto = Contrato_odonto.objects.all()
    contratos_nutri = Contrato_nutricionista.objects.all()
    objeto_contrato_odonto = Contrato_odonto

    #variaveis da funcao atual
    tamanho_clientes = len(clientes)
    tamanho_contrato_odonto = len(contratos_odonto)


    i=1

    soma_jan, soma_fev, soma_mar, soma_abr, soma_mai, soma_jun, soma_jul, soma_ago, soma_set, soma_out, soma_nov, soma_dez = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    hoje=''
    try:
        while i <= tamanho_contrato_odonto:

            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 1:
                soma_jan = soma_jan+objeto_contrato_odonto.objects.get(pk=i).plane_value
                hoje = objeto_contrato_odonto.objects.get(pk=i).date_today

            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 2:
                soma_fev = soma_fev+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 3:
                soma_mar = soma_mar+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 4:
                soma_abr = soma_abr+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 5:
                soma_mai = soma_mai+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 6:
                soma_jun = soma_jun+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 7:
                soma_jul = soma_jul+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 8:
                soma_ago = soma_ago+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 9:
                soma_set = soma_set+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 10:
                soma_out = soma_out+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 11:
                soma_nov = soma_nov+objeto_contrato_odonto.objects.get(pk=i).plane_value


            if objeto_contrato_odonto.objects.get(pk=i).format_monts()== 12:
                soma_dez = soma_dez+objeto_contrato_odonto.objects.get(pk=i).plane_value

            i = i + 1

        return render(request, "index.html", {'soma_janeiro_contratos': soma_jan,
                                          'soma_fevereiro_contratos':soma_fev,
                                          'soma_marco_contratos':soma_mar,
                                          'soma_abril_contratos':soma_abr,
                                          'soma_maio_contratos':soma_mai,
                                          'soma_junho_contratos':soma_jun,
                                          'soma_julho_contratos':soma_jul,
                                          'soma_agosto_contratos':soma_ago,
                                          'soma_setembro_contratos':soma_set,
                                          'soma_outrubro_contratos':soma_out,
                                          'soma_novembro_contratos':soma_nov,
                                          'soma_dezembro_contratos':soma_dez,
                                              'hoje':hoje})

    except objeto_contrato_odonto.DoesNotExist:
        raise Http404('Sem Contratos Registrados no momento')

@login_required(login_url='/login/')
def insere_profissional(request):

    if not request.user.has_perm('app_base.add_Profissionais'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = FormInsereProfissionais(request.POST)
        if form.is_valid():
            item = form.save(commit = False)
            item.user = request.user
            item.save()
            messages.success(request, 'Inserido com sucesso!')
            return render(request, 'salvo.html')
    else:
        form = FormInsereProfissionais()
    return render(request, 'paginas_app_base/insere_dentista.html', {'form': form})

@login_required(login_url='/login/')
def edita_profissional(request, nr_item):
    item = Profissionais.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsereProfissionais(request.POST, request.FILES, instance = item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item':item })
    else:
        form = FormInsereProfissionais(instance = item)        
    return render(request, 'paginas_app_base/insere_dentista.html', {'form':form})

@login_required(login_url='/login/')
def insere_funcionario(request):
    if not request.user.has_perm('app_base.add_Funcionario'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = FormInsereFuncionario(request.POST)
        if form.is_valid():
            item = form.save(commit = False)
            item.user = request.user
            item.save()
            messages.success(request, 'Inserido com sucesso!')
            return render(request, 'salvo.html')
    else:
        form = FormInsereFuncionario()
    return render(request, 'paginas_app_base/insere_funcionario.html', {'form': form})

@login_required(login_url='/login/')
def edita_funcionario(request,nr_item):
    item = Funcionario.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsereFuncionario(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormInsereFuncionario(instance=item)
    return render(request, 'paginas_app_base/insere_funcionario.html', {'form': form})

@login_required(login_url='/login/')
def edita_cliente(request,nr_item):
    item = Cliente.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsereCliente(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormInsereCliente(instance=item)
    return render(request, 'paginas_app_base/insere_cliente.html', {'form': form})

@login_required(login_url='/login/')
def insere_cliente(request):
    if request.method == 'POST':
        form = FormInsereCliente(request.POST)
        if form.is_valid():
            item = form.save(commit= False)
            item.user = request.user
            item.save()
            messages.success(request, 'Inserido com sucesso!')
            return render(request, 'salvo.html')
    else:
        form = FormInsereCliente()
    return render(request, 'paginas_app_base/insere_cliente.html', {'form': form})
@login_required(login_url='/login/')
def insere_contato_cliente(request):
    if request.method == 'POST':
        form = FormInsereContatoCliente(request.POST)
        if form.is_valid():
            item = form.save(commit= False)
            item.user = request.user
            item.save()
            messages.success(request, 'Inserido com sucesso!')
            return render(request, 'salvo.html')
    else:
        form = FormInsereContatoCliente()
    return render(request, 'paginas_app_base/Insere_Contato_Cliente.html', {'form': form})

@login_required(login_url='/login/')
def detalha_profissional(request, nr_item):
    dentista = ''
    try:
        item = Profissionais.objects.get(pk=nr_item)
        if item.professional_as == 'Dentista':
            dentista = item
    except Profissionais.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request,"paginas_app_base/item_dentista.html",{'dentista':dentista})

@login_required(login_url='/login/')
def detalha_funcinario(request, nr_item):
    try:
        item = Funcionario.objects.get(pk=nr_item)
    except Funcionario.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_base/item_funcionario.html", {'item': item})

@login_required(login_url='/login/')
def detalha_cliente(request, nr_item):
    try:
        item = Cliente.objects.get(pk=nr_item)
    except Cliente.DoesNotExist:
        raise Http404('Sem Registro!')
    return render(request, "paginas_app_base/item_cliente.html", {'item': item})

@login_required(login_url='/login/')
def verifica_cortesia_odonto(request,nr_item):
    '''
        A funcao esta correta!
    '''
    try:
        item = RecebimentoPlanoOdonto.objects.get(pk=nr_item)
        contrato_item = Contrato_odonto.objects.get(pk=item.name_client.id)
        cortesia = contrato_item.cortesia
        if item.TotalPagoTratamento >= 80:
            contrato_item.cortesia = True
            contrato_item.save()
            return render(request,"paginas_app_base/cortesia.html", {'cortesia':cortesia})
        else:
            return False
    except RecebimentoPlanoOdonto.DoesNotExist:
        raise Http404('Sem Contratos para verificar!')
