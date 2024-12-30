from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.logar, name='login'),
    path('cadastro', views.cadastrar, name='cadastro'),



]
