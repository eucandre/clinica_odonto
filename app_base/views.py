from django.shortcuts import *
from app_base.forms import *
from django.http import *
from django.core.paginator import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app_atendimento.models import *
from app_atendimento.models import *
from app_base.models import *


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
    jan, fev, mar, abr, mai, jun = 0, 0, 0, 0, 0, 0
    jul, ago, set, out, nov, dez = 0, 0, 0, 0, 0, 0
    
    janOr, fevOr, marOr, abrOr, maiOr, junOr = 0, 0, 0, 0, 0, 0
    julOr, agoOr, setOr, outOr, novOr, dezOr = 0, 0, 0, 0, 0, 0
    #--app_base--#
    hst_cliente = Cliente.history.all()[0]
    hst_profissionais = Profissionais.history.all()[0]
    hst_funcionario = Funcionario.history.all()[0]
    hst_contatos_clientes_indicacoes = Cotatos_Clientes_indicacoes.history.all()[0]
    #--app_atendimento--#
    hst_relatorio_exame_odonto = relatorio_exame_odonto.history.all()[0]
    hst_relatorio_exame_psico = relatorio_exame_psico.history.all()[0]
    hst_relatorio_exame_nutri = relatorio_exame_nutri.history.all()[0]
    hst_agendamento_plano_odonto = agendamemto_plano_odonto.history.all()[0]
    hst_agendamento_plano_nutri = agendamemto_plano_nutri.history.all()[0]
    hst_agendamento_plano_psico = agendamemto_plano_psico.history.all()[0]
    hst_agendamento_simples = agendamento_simples.history.all()[0]
    hst_agendamento_plano_filiado = agendamento_plano_filiado.history.all()[0]
    hst_relatorio_exame_odonto_continuado = relatorio_exame_odonto_continuado.history.all()[0]
    hst_relatorio_exame_psico_continuado = relatorio_exame_psico_continuado.history.all()[0]
    hst_relatorio_exame_nutri_continuado = relatorio_exame_nutri_continuado.history.all()[0]
    #--app_campanha--#
    contrato_novo = 0
    indicacoes = Cotatos_Clientes_indicacoes.objects.all()
    seg, ter, qua, qui, sex = 0, 0, 0, 0, 0
    sab = 0
    i = 1
    j = 1

    while i <= len(Contrato_odonto.objects.all()):
        objCO = Contrato_odonto.objects.get(pk=i)
        if objCO.format_monts()==1:
            jan = objCO.value_tratment()
            contrato_novo = contrato_novo + jan

        if objCO.format_monts()==2:
            fev = objCO.value_tratment()
            contrato_novo = contrato_novo + fev

        if objCO.format_monts()==3:
            mar = objCO.value_tratment()
            contrato_novo = contrato_novo + mar
        if objCO.format_monts()==4:
            abr = objCO.value_tratment()
            contrato_novo = contrato_novo + abr

        if objCO.format_monts()==5:
            mai = objCO.value_tratment()
            contrato_novo = contrato_novo + mai

        if objCO.format_monts()==6:
            jun = objCO.value_tratment()
            contrato_novo = contrato_novo + jun
        if objCO.format_monts()==7:
            jul = objCO.value_tratment()
            contrato_novo = contrato_novo +jul

        if objCO.format_monts()==8:
            ago = objCO.value_tratment()
            contrato_novo = contrato_novo+ago

        if objCO.format_monts()==9:
            set = objCO.value_tratment()
            contrato_novo = contrato_novo + set

        if objCO.format_monts()==10:
            out = objCO.value_tratment()
            contrato_novo = contrato_novo + out

        if objCO.format_monts()==11:
            nov = objCO.value_tratment()
            contrato_novo = contrato_novo + nov

        if objCO.format_monts()==12:
            dez = objCO.value_tratment()
            contrato_novo = contrato_novo + dez

        i = i + 1
    while j <=len(Orcamento_Plano_Odonto.objects.all()):
        objOO = Orcamento_Plano_Odonto.objects.get(pk=j)

        if objOO.format_date()==1:
            janOr = janOr+objOO.plane_value()

        if objOO.format_date()==2:
            fevOr = fevOr+objOO.plane_value()

        if objOO.format_date()==3:
            marOr = marOr+objOO.plane_value()

        if objOO.format_date()==4:
            abrOr = abrOr+objOO.plane_value()

        if objOO.format_date()==5:
            maiOr = maiOr+objOO.plane_value()

        if objOO.format_date()==6:
            junOr = junOr+objOO.plane_value()

        if objOO.format_date()==7:
            julOr = julOr+objOO.plane_value()

        if objOO.format_date()==8:
            agoOr = agoOr+objOO.plane_value()

        if objOO.format_date()==9:
            setOr = setOr+objOO.plane_value()

        if objOO.format_date()==10:
            outOr = outOr+objOO.plane_value()

        if objOO.format_date()==11:
            novOr = novOr+objOO.plane_value()

        if objOO.format_date()==12:
            dezOr = dezOr+objOO.plane_value()

        j = j + 1

    hoje = datetime.today().month
    #if len(agendamemto_plano_odonto.objects.all())==0:
    #   return HttpResponseRedirect('/agendamentos_plano_odonto/')
    #else:
    #    a=1
     #   while a <= len(agendamemto_plano_odonto.objects.all()):
     #       agendaobj = agendamemto_plano_odonto.objects.get(pk=a)
     #       a=a+1
    return render(request, 'index.html',{'Janeiro':jan,'Fevereiro':fev,'Marco':mar,'Abril':abr,'Maio':mai,'Junho':jun
        ,'Julho':jul,'Agosto':ago, 'Setembro':set, 'Outubro':out, 'Novembro':nov, 'Dezembro':dez,
                                         'janeiro':janOr,'fevereiro':fevOr,'marco':maiOr,'abril':abrOr,'maio':maiOr,'junho':junOr,'julho':julOr,
                                        'agosto':agoOr,'setembro':setOr,'outubro':outOr,'novembro':novOr,'dezembro':dezOr,
                                         'contratos_odonto':contrato_novo, 'hoje':hoje, 'indicacoes':len(indicacoes)
                                         ,'historia':hst_cliente})

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
def verifica_cortesia_odonto(nr_item):
    '''
        A funcao esta correta!
    '''
    try:
        item = RecebimentoPlanoOdonto.objects.get(pk=nr_item)
        contrato_item = Contrato_odonto.objects.get(pk=item.name_client.id)
        # cortesia = contrato_item.cortesia
        if item.TotalPagoTratamento >= 80:
            contrato_item.cortesia = True
            contrato_item.save()
            return True
        else:
            return False
    except RecebimentoPlanoOdonto.DoesNotExist:
        return None
