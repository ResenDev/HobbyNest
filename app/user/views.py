from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Usuario
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UsuarioForm
class CadastroCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'user/auth/cadastro_user.html'
    success_url = reverse_lazy('user:login')
    
    
    
    def form_valid(self, form):
        messages.success(self.request, "Usuário criado com sucesso!")
        self.object = form.save()
        return HttpResponseRedirect(self.success_url) 
    


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
            return HttpResponseRedirect('itens/meus_itens/')
            # envia para a lista de itens
        else:
            messages.error(request, "Dados inválidos!")
            return redirect('user:login')


@login_required
def deslogar(request):
    logout(request)
    return redirect('user:login')
