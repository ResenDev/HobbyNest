from django.urls import path
from item import views

app_name = 'item'

urlpatterns = [
    path('meus_itens', views.ItemListView, name='meus_itens'),
    path('cadastrar', views.ItemCreateView, name='cadastrar_item'),
    path('atualizar', views.ItemUpdateView, name='atualizar_item'),
    path('deletar', views.ItemDeleteView, name='deletar_item'),
]
