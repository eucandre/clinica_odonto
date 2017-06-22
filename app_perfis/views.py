from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import  User,UserCreationForm,UserChangeForm# Formulario de criacao de usuarios
from django.contrib.auth.decorators import login_required
from django.core.paginator import *

@login_required(login_url='/login/')
def registrar(request):

    # Se dados forem passados via POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados
            return HttpResponseRedirect("/") # redireciona para a tela de login
        else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            return render(request, "registrar.html", {"form": form})

    # se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
    return render(request, "registrar.html", {"form": UserCreationForm() })

def lista_usuarios(request):
    usuarios = User.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios, 10)
    try:
        p_usuarios = paginator.page(page)
    except PageNotAnInteger:
        p_usuarios = paginator.page(1)
    except EmptyPage:
        p_usuarios = paginator.page(paginator.num_pages)
    return render(request, 'lista_usuarios.html',
                  {'p_usuarios': p_usuarios})

def edita_usuario(request, nr):
    item = User.objects.get(pk=nr)
    if request.method =='POST':
        form = UserChangeForm(request.POST, request.FILES, instance = item)
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados
            return HttpResponseRedirect("/") # redireciona para a tela de login
    else:
            # mostra novamente o formulario de cadastro com os erros do formulario atual
            form = UserChangeForm(instance = item)
    return render(request, "edita_user.html", {"form": form})