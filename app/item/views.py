from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy

# Create your views here.


class ItemListView(LoginRequiredMixin, ListView):
    template_name = 'item/lista_itens.html'  # onde será renderizada a lista
    model = Item
    paginate_by = 10
    context_object_name = 'itens'  # nome da lista de objetos

    def get_queryset(self):
        # filtra os itens do usuário logado
        return Item.objects.filter(user_FK_id=self.request.user)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'item/edita_item.html'
    model = Item
    fields = ['id', 'titulo', 'categoria',
              'marca', 'descricao_item', 'ano_aquisicao']


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/cadastro_item.html'
    success_url = reverse_lazy('item:meus_itens')
    

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'item/deletar_item.html'
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy("item:meus_itens")

# MODEL +  Class-Based View = Nome da classe
