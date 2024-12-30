from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse
from .models import Usuario


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
        return HttpResponse('Criado com sucesso!')


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

        if usuario:  # caso seja válido
            login(request, usuario)
            # enviar pra os itens
        else:
            return HttpResponse('Dados inválidos!')


def deslogar(request):
    logout(request)
# @login_required(login_url='user/auth/login.html')
