from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Usuario

@login_required
def cadastrar(request):
    if request.method == "GET":
        return render(
            request,
            'user/auth/cadastro_user.html'
        )
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')  # pbkdf2_sha256

        senha_hash = make_password(password)
        usuario = Usuario.objects.create(first_name=first_name, last_name=last_name,
                                         email=email, username=username, password=senha_hash
                                         )
        usuario.save()
        return messages.success('Criado com sucesso!')


def logar(request):
    if request.method == "GET":
        return render(
            request,
            'user/auth/login.html'
        )
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')  # pbkdf2_sha256

        usuario = authenticate(username=username, password=password)
        messages.error(request, "Dados inválidos!")
        if usuario:  # caso seja válido
            login(request, usuario)
            return HttpResponseRedirect('itens/meus_itens/')
            # envia para a lista de itens
        else:
            return redirect('user:login')


@login_required
def deslogar(request):
    logout(request)
    return redirect('user:login')
