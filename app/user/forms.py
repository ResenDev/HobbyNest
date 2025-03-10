from django import forms
from .models import Usuario
from django.contrib.auth.hashers import make_password
"""Utilizado no Formulário de Cadastro"""
class UsuarioForm(forms.ModelForm):
    
    username = forms.CharField(
         max_length=150,
         required= True,
         
    )
    password = forms.CharField(
         max_length=128,
         required= True,  
    )

    class Meta:
        model = Usuario
        fields = ['first_name','last_name','email','username','password']
        
    
    def clean_password(self):  # hasheia a senha
        password = self.cleaned_data['password']
        if len(password)>=1:
            hash = make_password(password)
            password = hash
        return password

    def clean_username(self):
        # recebe dado do formulário
        username = self.cleaned_data['username']
        # *A Fazer* verifica se o usuario informado existe no banco
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("Esse usuário já existe!")
        elif not username:
            raise forms.ValidationError("O username não pode ser vazio!")  
        return username    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Esse email já pertence a uma conta!")
        return email
    
