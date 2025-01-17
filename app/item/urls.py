from django.urls import path
from item import views

app_name = 'item'

urlpatterns = [
    path('meus_itens/', views.ItemListView.as_view(), name='meus_itens'),
    path('cadastrar/', views.ItemCreateView.as_view(), name='cadastrar_item'),
    path('detalhe/<int:pk>/', views.ItemDetailView.as_view(), name='detalhar_item'),
    path('atualizar/<int:pk>/', views.ItemUpdateView.as_view(), name='atualizar_item'),
    path('deletar/<int:pk>/', views.ItemDeleteView.as_view(), name='deletar_item'),
]
