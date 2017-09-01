import django.http
from django.shortcuts import render
from app_estoque.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import *

@login_required(login_url='/login/')
def insere_fornecedor(request):
    if request.method == 'POST':
        form = FormInsererFornecedor(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request,'salvo.html')
    else:
        form = FormInsererFornecedor()
    return render(request, 'paginas_app_estoque/insere_fornecedor.html',{'form':form})

@login_required(login_url='/login/')
def edita_fornecedor(request, nr_item):
    item = Fornecedor.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsererFornecedor(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormInsererFornecedor(instance=item)
    return render(request, 'paginas_app_estoque/insere_fornecedor.html', {'form': form})

@login_required(login_url='/login/')
def lista_fornecedor(request):
    fornecedor = Fornecedor.objects.all()
    page = request.GET.get('page', 1)
    paginatior = Paginator(fornecedor, 10)
    try:
        p_fornecedor = paginatior.page(page)
    except PageNotAnInteger:
        p_fornecedor = paginatior.page(1)
    except EmptyPage:
        p_fornecedor = paginatior.page(paginatior.num_pages)
    return render(request, "paginas_app_estoque/lista_fornecedor.html", {"fornecedor": p_fornecedor})

@login_required(login_url='/login/')
def detalha_fornecedor(request, nr_item):
    try:
        item = Fornecedor.objects.get(pk=nr_item)
    except Fornecedor.DoesNotExist:
        raise django.http.Http404('Sem Registro!')
    return render(request, "paginas_app_estoque/item_fornecedor.html", {'item': item})

@login_required(login_url='/login/')
def insere_produto(request):
    if request.method == 'POST':
        form = FormInsereProduto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormInsereProduto()
    return render(request, 'paginas_app_estoque/insere_produto.html', {'form':form})

@login_required(login_url='/login/')
def edita_produto(request, nr_item):
    item = Produto.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsereProduto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormInsereProduto(instance=item)
    return render(request, 'paginas_app_estoque/insere_fornecedor.html', {'form': form})

@login_required(login_url='/login/')
def lista_produto(request):
    produto = Produto.objects.all()
    page = request.GET.get('page', 1)
    paginatior = Paginator(produto, 10)
    try:
        p_produto = paginatior.page(page)
    except PageNotAnInteger:
        p_produto = paginatior.page(1)
    except EmptyPage:
        p_produto = paginatior.page(paginatior.num_pages)
    return render(request, "paginas_app_estoque/lista_produto.html", {"produto": p_produto})

@login_required(login_url='/login/')
def detalha_produto(request, nr_item):
    try:
        item = Produto.objects.get(pk=nr_item)
    except Produto.DoesNotExist:
        raise django.http.Http404('Sem Registro!')
    return render(request, "paginas_app_estoque/item_produto.html", {'item': item})

@login_required(login_url='/login/')
def insere_retira_produtos(request):
    if request.method == 'POST':
        form = FormInsereRetiraProduto(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormInsereRetiraProduto()
    return render(request, 'paginas_app_estoque/insere_retira_produtos.html', {'form':form})

@login_required(login_url='/login/')
def edita_retira_produto(request, nr_item):
    item = Retira_Produto.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsereRetiraProduto(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormInsereRetiraProduto(instance=item)
    return render(request, 'paginas_app_estoque/insere_retira_produtos.html', {'form': form})

@login_required(login_url='/login/')
def lista_retira_produto(request):
    retira_produto = Retira_Produto.objects.all()
    page = request.GET.get('page', 1)
    paginatior = Paginator(retira_produto, 10)
    try:
        p_retira_produto = paginatior.page(page)
    except PageNotAnInteger:
        p_retira_produto = paginatior.page(1)
    except EmptyPage:
        p_retira_produto = paginatior.page(paginatior.num_pages)
    return render(request, "paginas_app_estoque/lista_retira_produto.html", {"retira_produto": p_retira_produto})

@login_required(login_url='/login/')
def detalha_retira_produto(request, nr_item):
    try:
        item = Retira_Produto.objects.get(pk=nr_item)
    except Retira_Produto.DoesNotExist:
        raise django.http.Http404('Sem Registro!')
    return render(request, "paginas_app_estoque/item_retira_produto.html", {'item': item})

@login_required(login_url='/login/')
def insere_compra_produtos(request):
    if request.method == 'POST':
        form = FormInsereCompraProdutos(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            # forn = form.save(commit=False)
            # forn.provider = request.provider
            # forn.save()
            item.user = request.user
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormInsereCompraProdutos()
    return render(request, 'paginas_app_estoque/insere_compra_produtos.html', {'form':form})

@login_required(login_url='/login/')
def edita_compra_produtos(request, nr_item):
    item = Compra_Produto.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormInsereCompraProdutos(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alterado com sucesso!')
            return render(request, 'salvo.html', {'item': item})
    else:
        form = FormInsereCompraProdutos(instance=item)
    return render(request, 'paginas_app_estoque/insere_compra_produtos.html', {'form': form})

@login_required(login_url='/login/')
def lista_compra_produto(request):
    compra_produto = Fornecedor.objects.all()
    page = request.GET.get('page', 1)
    paginatior = Paginator(compra_produto, 10)
    try:
        p_compra_produto = paginatior.page(page)
    except PageNotAnInteger:
        p_compra_produto = paginatior.page(1)
    except EmptyPage:
        p_compra_produto = paginatior.page(paginatior.num_pages)
    return render(request, "paginas_app_estoque/lista_compra_produto.html", {"compra_produto": p_compra_produto})

@login_required(login_url='/login/')
def detalha_compra_produtos(request,nr_item):
    try:
        item = Compra_Produto.objects.get(pk=nr_item)
    except Compra_Produto.DoesNotExist:
        raise django.http.Http404('Sem Registro!')
    return render(request, "paginas_app_estoque/item_retira_produto.html", {'item': item})

def monte():
    obj_retirada = Retira_Produto.objects.get(pk=len(Retira_Produto.objects.all()))
    obj_compra = Compra_Produto.objects.get(pk=len(Compra_Produto.objects.all()))
    valorRetirado = int(obj_retirada.amount_withdrawal)
    valorComprado= int(obj_compra.amout_purchased)
    return valorComprado - valorRetirado

@login_required(login_url='/login/')
def atualizaMontante(request):

    if request.method == 'POST':
        form = FormMontante(request.POST)
        if form.is_valid():
            item = form.save(commit= False)
            item.user = request.user
            item.montante = monte()
            item.save()
            return render(request, 'salvo.html')
    else:
        form = FormMontante()
    return render(request, 'paginas_app_estoque/montante.html', {'form':form})