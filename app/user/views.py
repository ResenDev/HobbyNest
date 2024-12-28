from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponse

def logar (request):
    if request.method == "GET":
        return render(
        request,
        'user/auth/login.html'
        )
    elif request.method  == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username,password=password)

        if usuario: #caso seja válido
            login(request,usuario)
        else:
            return HttpResponse('Dados inválidos!')

def deslogar(request):
    logout(request)
##@login_required(login_url='user/auth/login.html')