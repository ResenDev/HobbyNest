from django.contrib.auth.mixins import LoginRequiredMixin #é equivalente a um @login_required, mas para CBV.
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import CreateView
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.shortcuts import render
from django.http import JsonResponse
class ItemListView(LoginRequiredMixin, ListView):
    # template onde será renderizada a lista
    template_name = 'item/lista_itens.html'
    model = Item
    paginate_by = 10  # limite de itens por página
    context_object_name = 'itens'  # nome da lista de objetos que será passada ao html
    def get_queryset(self):
        # retorna os itens do usuário logado (que está fazendo o request), ordenado pelo q foi atualizado mais recente
        return Item.objects.order_by('-updated_at').filter(user_FK_id=self.request.user) # pylint: disable=E1101

class ItemDetailView(LoginRequiredMixin,DetailView):
    model = Item
    template_name ='item/detalhe_item.html'
    context_object_name = 'item' 

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/cadastro_item.html'
    success_url = reverse_lazy('item:meus_itens')
    
    def form_valid(self, form):
        form.instance.user_FK = self.request.user #atribui o usuario logado ao campo user_FK
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Dados enviados:", self.request.POST)
        print("Erros do formulário:", form.errors)
        
        return super().form_invalid(form)
        
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class=ItemForm
    template_name = 'item/edita_item.html'
    success_url = reverse_lazy('item:meus_itens')
    context_object_name = 'item' 
    def form_valid(self,form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Dados enviados:", self.request.POST)
        print("Erros do formulário:", form.errors)
        
        return super().form_invalid(form)
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'item/deletar_item.html'
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('item:meus_itens')
# MODEL +  Class-Based View = Nome da classe
