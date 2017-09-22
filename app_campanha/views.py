from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def campanha_insere(request):
    if request.method == 'POST':
        form = FormCampanha(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.info(request, "Salvo com sucesso!")
            return render(request, 'salvo.html')
    else:
        form = FormCampanha()
    return render(request, 'paginas_app_campanha/camapanha_venda.html', {"form": form})

@login_required(login_url='/login/')
def edita_campanha(request, nr_item):
    item = campanha.objects.get(pk=nr_item)
    if request.method == 'POST':
        form = FormCampanha(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.info(request, "Salvo com sucesso!")
            return render(request, 'salvo.html')
    else:
        form = FormCampanha(instance=item)
    return render(request, 'paginas_app_campanha/camapanha_venda.html', {"form": form})

@login_required(login_url='/login/')
def detalha_campanha(request, nr_item):
    try:
        item = campanha.objects.get(pk=nr_item)
    except campanha.DoesNotExist:
        raise Http404
    return render(request, 'paginas_app_campanha/item_campanha.html',{'item':item})



@login_required(login_url='/login/')
def lista_camapanha(request):
    obj = campanha.objects.all()
    page = request.GET.get('page', 1)
    paginatior = Paginator(obj, 10)
    try:
        p_campanha = paginatior.page(page)
    except PageNotAnInteger:
        p_campanha = paginatior.page(1)
    except EmptyPage:
        p_campanha = paginatior.page(paginatior.num_pages)

    return render(request, "paginas_app_campanha/lista_campanhas.html", {"campanha_insere": p_campanha})

