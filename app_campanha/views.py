from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def campanhas(request):
    if request.method == 'POST':
        form = FormCampanha(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            messages.info(request, "Salvo com sucesso!")
            return render(request, 'salvo.html')
    else:
        form = FormCampanha()
    return render(request, 'paginas_app_campanha/camapanha_venda.html', {"form": form})

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

    return render(request, "paginas_app_campanha/lista_campanhas.html", {"campanhas": p_campanha})

