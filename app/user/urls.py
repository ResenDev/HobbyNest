from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('cadastro/', views.CadastroCreateView.as_view(), name='cadastro'),



]
