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
    permissao_profissional = request.user.has_perm('app_base.add_Profissionais')
    permissao_funcionario = request.user.has_perm('app_base.add_Funcionario')
    permissao_cliente = request.user.has_perm('app_base.add_Cliente')



    """
        A tarefa desta funcao eh montar o dashboard do sistema, trazer os dados e montar o grafico tambem.
        Estas sao as vairaveis desta funcao : orcament_odonto,value_orcament,sum,total_tratments ,date_initial_orcament, today
    """
    sum_jan, sum_fev, sum_marc, sum_abr, sum_mai, sum_jun, sum_jul, sum_ago, sum_set, sum_out, sum_nov, sum_dec = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    sum_contrato_jan, sum_contrato_fev, sum_contrato_marc, sum_contrato_abr, sum_contrato_mai, sum_contrato_jun, sum_contrato_jul, sum_contrato_ago, sum_contrato_set, sum_contrato_out, sum_contrato_nov, sum_contrato_dec = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    i=1

    try:
        while i <= len(OrcamentoPlanoOdontologico.objects.all()):
            if OrcamentoPlanoOdontologico.objects.get(pk=i).format_date()==1:
                sum_jan = sum_jan+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date()==2:
                sum_fev = sum_fev+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 3:
                sum_marc = sum_marc+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 4:
                sum_abr = sum_abr+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 5:
                sum_mai = sum_mai+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 6:
                sum_jun = sum_jun+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 7:
                sum_jul = sum_jul+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_ago+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_set+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_out+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_nov+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoOdontologico.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_dec+OrcamentoPlanoOdontologico.objects.get(pk=i).value_tratment
            i+=1
    except OrcamentoPlanoOdontologico.DoesNotExist:
        raise Http404()

    try:
        while i <= (len(OrcamentoPlanoNutri.objects.all())):
            if OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 1:
                sum_jan = sum_jan + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 2:
                sum_fev = sum_fev + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 3:
                sum_marc = sum_marc + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 4:
                sum_abr = sum_abr + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 5:
                sum_mai = sum_mai + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 6:
                sum_jun = sum_jun + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 7:
                sum_jul = sum_jul + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_ago + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 9:
                sum_set = sum_set + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 10:
                sum_out = sum_out + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 11:
                sum_nov = sum_nov + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoNutri.objects.get(pk=i).format_date() == 12:
                sum_dec = sum_dec + OrcamentoPlanoNutri.objects.get(pk=i).value_tratment
            i += 1
    except OrcamentoPlanoNutri.DoesNotExist:
        raise Http404()

    try:
        while i <= (len(OrcamentoPlanoPsico.objects.all())):
            if OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 1:
                sum_jan = sum_jan + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 2:
                sum_fev = sum_fev + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 3:
                sum_marc = sum_marc + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 4:
                sum_abr = sum_abr + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 5:
                sum_mai = sum_mai + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 6:
                sum_jun = sum_jun + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 7:
                sum_jul = sum_jul + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 8:
                sum_ago = sum_ago + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 9:
                sum_set = sum_set + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 10:
                sum_out = sum_out + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 11:
                sum_nov = sum_nov + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            elif OrcamentoPlanoPsico.objects.get(pk=i).format_date() == 12:
                sum_dec = sum_dec + OrcamentoPlanoPsico.objects.get(pk=i).value_tratment
            i += 1
    except OrcamentoPlanoPsico.DoesNotExist:
        raise Http404()

    try:
        while i <= (len(Contrato_odonto.objects.all())):
            if Contrato_odonto.objects.get(pk=i).format_date() == 1:
                sum_contrato_jan = sum_contrato_jan + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 2:
                sum_contrato_fev = sum_contrato_fev + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 3:
                sum_contrato_marc = sum_contrato_marc + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 4:
                sum_contrato_abr = sum_contrato_abr + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 5:
                sum_contrato_mai = sum_contrato_mai + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 6:
                sum_contrato_jun = sum_contrato_jun + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 7:
                sum_contrato_jul = sum_contrato_jul + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 8:
                sum_contrato_ago = sum_contrato_ago + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 9:
                sum_contrato_set = sum_contrato_set + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 10:
                sum_contrato_out = sum_contrato_out + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 11:
                sum_contrato_nov = sum_contrato_nov + Contrato_odonto.objects.get(pk=i).value_tratment
            elif Contrato_odonto.objects.get(pk=i).format_date() == 12:
                sum_contrato_dec = sum_contrato_dec + Contrato_odonto.objects.get(pk=i).value_tratment
            i += 1
    except Contrato_odonto.DoesNotExist:
        raise Http404()

    try:
        while i <= (len(Contrato_psicologo.objects.all())):
            if Contrato_psicologo.objects.get(pk=i).format_date() == 1:
                sum_contrato_jan = sum_contrato_jan + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 2:
                sum_contrato_fev = sum_contrato_fev + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 3:
                sum_contrato_marc = sum_contrato_marc + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 4:
                sum_contrato_abr = sum_contrato_abr + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 5:
                sum_contrato_mai = sum_contrato_mai + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 6:
                sum_contrato_jun = sum_contrato_jun + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 7:
                sum_contrato_jul = sum_contrato_jul + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 8:
                sum_contrato_ago = sum_contrato_ago + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 9:
                sum_contrato_set = sum_contrato_set + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 10:
                sum_contrato_out = sum_contrato_out + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 11:
                sum_contrato_nov = sum_contrato_nov + Contrato_psicologo.objects.get(pk=i).value_tratment
            elif Contrato_psicologo.objects.get(pk=i).format_date() == 12:
                sum_contrato_dec = sum_contrato_dec + Contrato_psicologo.objects.get(pk=i).value_tratment
            i += 1
    except Contrato_psicologo.DoesNotExist:
        raise Http404()

    try:
        while i <= (len(Contrato_nutricionista.objects.all())):
            if Contrato_nutricionista.objects.get(pk=i).format_date() == 1:
                sum_contrato_jan = sum_contrato_jan + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 2:
                sum_contrato_fev = sum_contrato_fev + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 3:
                sum_contrato_marc = sum_contrato_marc + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 4:
                sum_contrato_abr = sum_contrato_abr + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 5:
                sum_contrato_mai = sum_contrato_mai + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 6:
                sum_contrato_jun = sum_contrato_jun + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 7:
                sum_contrato_jul = sum_contrato_jul + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 8:
                sum_contrato_ago = sum_contrato_ago + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 9:
                sum_contrato_set = sum_contrato_set + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 10:
                sum_contrato_out = sum_contrato_out + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 11:
                sum_contrato_nov = sum_contrato_nov + Contrato_nutricionista.objects.get(pk=i).value_tratment
            elif Contrato_nutricionista.objects.get(pk=i).format_date() == 12:
                sum_contrato_dec = sum_contrato_dec + Contrato_nutricionista.objects.get(pk=i).value_tratment
            i += 1
    except Contrato_nutricionista.DoesNotExist:
        raise Http404()


    total_orcamentos = sum_jan+ sum_fev+ sum_marc+ sum_abr+ sum_mai+ sum_jun+ sum_jul+ sum_ago+ sum_set+ sum_out+ sum_nov+ sum_dec

    total_contratos = sum_contrato_jan+ sum_contrato_fev+ sum_contrato_marc+ sum_contrato_abr+ sum_contrato_mai+ sum_contrato_jun+ sum_contrato_jul+ sum_contrato_ago+ sum_contrato_set+ sum_contrato_out+ sum_contrato_nov+ sum_contrato_dec

    if permissao_funcionario == False and permissao_profissional == True:
        pagamentos_planos = RecebimentoPlano.objects.all()

        return render(request, 'index_gerencia.html', {'recebimentos_plano':pagamentos_planos})

    if permissao_profissional == False:
        data_de_hoje = date.today()
        agendamentos_odonto = agendamemto_plano_odonto.objects.all().filter(date_atendence=data_de_hoje)

        return render(request,"index_atendente.html", {'agenda_odonto':agendamentos_odonto})
    else:
        return render(request, "index.html",{'orcamento_jan':sum_jan,'valor':total_orcamentos,
        'orcamento_fevereiro':sum_fev, 'orcamento_marco':sum_marc, 'orcamento_abril':sum_abr,
                                         'orcamento_maio':sum_mai, 'orcamento_junho':sum_jun,
                                         'orcamento_jul':sum_jul,'orcamento_agosto':sum_ago,'orcamento_setembro':sum_set,
                                         'orcamento_outubro':sum_out,'orcamento_novembro':sum_nov, 'orcamento_dezembro':sum_dec,
                                          'contrato_jan':sum_contrato_jan, 'contrato_fev':sum_contrato_fev, 'contrato_mar':sum_contrato_marc,
                                          'contrato_abril':sum_contrato_abr, 'contrato_maio':sum_contrato_mai, 'contrato_jun':sum_contrato_jun,
                                          'contrato_julho':sum_contrato_jul, 'contrato_agosto':sum_contrato_ago, 'contrato_setembro':sum_contrato_set,
                                          'contrato_outubro':sum_contrato_out, 'contrato_novembro':sum_contrato_nov, 'contrato_dezembro':sum_contrato_dec,
                                         'permissao_cliente':permissao_cliente, 'permissao_funcionario':permissao_funcionario,
                                         'permissao_profissional':permissao_profissional})

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

