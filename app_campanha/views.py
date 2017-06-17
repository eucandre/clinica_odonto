from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def campanha(request):
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
def camapanha_venda(request):
    if request.method =='POST':
        form = FormCampanhaVenda(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            messages.info(request, "Salvo com sucesso!")
            return render(request,'salvo.html')
    else:
        form = FormCampanhaVenda()
    return render(request, 'paginas_app_campanha/camapanha_venda.html', {"form":form})
