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
    if Contrato_odonto.objects.all() or Orcamento_Plano_Odonto.objects.all():

        jan = 0
        fev = 0
        mar = 0
        abr = 0
        mai = 0
        jun = 0
        jul = 0
        ago = 0
        set = 0
        out = 0
        nov = 0
        dez = 0

        janN = 0
        fevN = 0
        marN = 0
        abrN = 0
        maiN = 0
        junN = 0
        julN = 0
        agoN = 0
        setN = 0
        outN = 0
        novN = 0
        dezN = 0

        janP = 0
        fevP = 0
        marP = 0
        abrP = 0
        maiP = 0
        junP = 0
        julP = 0
        agoP = 0
        setP = 0
        outP = 0
        novP = 0
        dezP = 0

        janOrOdonto = 0
        fevOrOdonto = 0
        marOrOdonto = 0
        abrOrOdonto = 0
        maiOrOdonto = 0
        junOrOdonto = 0
        julOrOdonto = 0
        agoOrOdonto = 0
        setOrOdonto = 0
        outOrOdonto = 0
        novOrOdonto = 0
        dezOrOdonto = 0

        soma =0
        i= 1
        tamanho = len(Contrato_odonto.objects.all())
        while i<=tamanho:
            obje = Contrato_odonto.objects.get(pk=i)
            if obje.format_monts()==1:
                jan= soma+obje.value_tratment()

            elif obje.format_monts()==2:
                fev= soma+obje.value_tratment()

            elif obje.format_monts()==3:
                mar= soma+obje.value_tratment()

            elif obje.format_monts()==4:
                abr= soma+obje.value_tratment()

            elif obje.format_monts()==5:
                mai= soma+obje.value_tratment()

            elif obje.format_monts()==6:
                jun= soma+obje.value_tratment()

            elif obje.format_monts()==7:
                jul= soma+obje.value_tratment()

            elif obje.format_monts()==8:
                ago= soma+obje.value_tratment()

            elif obje.format_monts()==9:
                set= soma+obje.value_tratment()

            elif obje.format_monts()==10:
                out= soma+obje.value_tratment()

            elif obje.format_monts()==11:
                nov= soma+obje.value_tratment()

            elif obje.format_monts()==12:
                dez= soma+obje.value_tratment()
            i=i+1
    else:
        tamanho = 0
    if Contrato_nutricionista.objects.all():

        soma = 0
        n = 1
        tamanhoN = len(Contrato_nutricionista.objects.all())
        while n <= tamanhoN:
            objn= Contrato_nutricionista.objects.get(pk=n)
            if objn.format_monts()==1:
                janN= soma+objn.value_tratment()

            if objn.format_monts()==2:
                fevN= soma+objn.value_tratment()

            if objn.format_monts()==3:
                marN= soma+objn.value_tratment()

            if objn.format_monts()==4:
                abrN= soma+objn.value_tratment()

            if objn.format_monts()==5:
                maiN= soma+objn.value_tratment()

            if objn.format_monts()==6:
                junN= soma+objn.value_tratment()

            if objn.format_monts()==7:
                julN= soma+objn.value_tratment()

            if objn.format_monts()==8:
                agoN= soma+objn.value_tratment()

            if objn.format_monts()==9:
                setN= soma+objn.value_tratment()

            if objn.format_monts()==10:
                outN= soma+objn.value_tratment()

            if objn.format_monts()==11:
                novN= soma+objn.value_tratment()

            if objn.format_monts()==12:
                dezN= soma+objn.value_tratment()
    if Contrato_psicologo.objects.all():
        soma= 0
        k=1
        tamanhoP = len(Contrato_nutricionista.objects.all())
        while k <= tamanhoP:
            objp = Contrato_nutricionista.objects.get(pk=k)
            if objp.format_monts() == 1:
                janP = soma + objp.value_tratment()
                soma = janP

            if objp.format_monts() == 2:
                fevP = soma + objp.value_tratment()

            if objp.format_monts() == 3:
                marP = soma + objp.value_tratment()

            if objp.format_monts() == 4:
                abrP = soma + objp.value_tratment()

            if objp.format_monts() == 5:
                maiP = soma + objp.value_tratment()

            if objp.format_monts() == 6:
                junP = soma + objp.value_tratment()

            if objp.format_monts() == 7:
                julP = soma + objp.value_tratment()

            if objp.format_monts() == 8:
                agoP = soma + objp.value_tratment()

            if objp.format_monts() == 9:
                setP = soma + objp.value_tratment()

            if objp.format_monts() == 10:
                outP = soma + objp.value_tratment()

            if objp.format_monts() == 11:
                novP = soma + objp.value_tratment()

            if objp.format_monts() == 12:
                dezP = soma + objp.value_tratment()

    if Orcamento_Plano_Odonto.objects.all():
        soma = 0
        y = 1
        while y <= len(Orcamento_Plano_Odonto.objects.all()):
            objord = Orcamento_Plano_Odonto.objects.get(pk=y)
            if objord.format_date()== 1:
                janOrOdonto = objord.plane_value()+soma
                soma = janOrOdonto+soma
            if objord.format_date() == 2:
                fevOrOdonto = objord.plane_value()+soma
                soma = fevOrOdonto+soma

            if objord.format_date() == 3:
                marOrOdonto = objord.plane_value()+soma
                soma = marOrOdonto+soma

            if objord.format_date() == 4:
                abrOrOdonto = objord.plane_value()+soma
                soma = abrOrOdonto+soma

            if objord.format_date() == 5:
                maiOrOdonto = objord.plane_value()+soma
                soma = maiOrOdonto+soma

            if objord.format_date() == 6:
                junOrOdonto = objord.plane_value()+soma
                soma = junOrOdonto+soma

            if objord.format_date() == 7:
                julOrOdonto = objord.plane_value()+soma
                soma = julOrOdonto+soma

            if objord.format_date() == 8:
                agoOrOdonto = objord.plane_value()+soma
                soma = agoOrOdonto+soma

            if objord.format_date() == 9:
                setOrOdonto = objord.plane_value()+soma
                soma = setOrOdonto+soma

            if objord.format_date() == 10:
                outOrOdonto = objord.plane_value()+soma
                soma = outOrOdonto+soma

            if objord.format_date() == 11:
                novOrOdonto = objord.plane_value()+soma
                soma = novOrOdonto+soma

            if objord.format_date() == 12:
                devOrOdonto = objord.plane_value()+soma
                soma = devOrOdonto+soma

    return render(request, 'index.html',{'Janeiro':jan+janN+janP, 'Fevereiro':fev+fevN+fevP,
                                         'Marco':mar+marN+marP, 'Abril':abr+abrN+abrP, 'Maio':mai+maiN+maiP,
                                         'Junho':jun+junN+junP,'Julho':jul+julN+julP,'Agosto':ago+agoN+agoP, 'Setembro':set+setN+setP,
                                         'Outubro':out+outN+outP, 'Novembro':nov+novN+novP, 'Dezembro':dez+dezN+dezP,
                                         'orcamento_jan':janOrOdonto,'orcamento_fev':fevOrOdonto, 'orcamento_mar':marOrOdonto,
                                         'orcamento_abr':abrOrOdonto, 'orcamento_mai':maiOrOdonto, 'orcamento_jun':junOrOdonto,
                                         'orcamento_jul':julOrOdonto, 'orcamento_ago':agoOrOdonto, 'orcamento_set':setOrOdonto,
                                         'orcamento_out':outOrOdonto, 'orcamento_nov':novOrOdonto, 'orcamento_dez':dezOrOdonto})

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
