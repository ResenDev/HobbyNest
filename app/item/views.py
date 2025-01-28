from django.contrib.auth.mixins import LoginRequiredMixin #é equivalente a um @login_required, mas para CBV.
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import CreateView
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib  import messages
from django.core.paginator import Paginator,InvalidPage
from django.http import HttpResponseRedirect,HttpResponse
class MeuPaginator(Paginator):
    def page(self, number):
        try:
            number = self.validate_number(number)
        except InvalidPage: # engloba PageNotAnInteger e EmptyPage
            number = self.num_pages # retorna a última página
        return super().page(number)  
class ItemListView(LoginRequiredMixin, ListView):
    # template onde será renderizada a lista
    template_name = 'item/lista_itens.html'
    model = Item
    paginator_class = MeuPaginator
    paginate_by = 10  # limite de itens por página
    context_object_name = 'itens'  # nome da lista de objetos que será passada ao html
    #TODO resolver erro das urls
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
        form.instance.user_FK = self.request.user # atribui o usuario logado ao campo user_FK
        messages.success(self.request,"Item criado com sucesso!")
        self.object = form.save()# salva o objeto no banco
        return HttpResponse('<script>window.location.reload();</script>')  # atualiza a página usando js
 # salva e redireciona para a success_url
    
    def form_invalid(self, form):
        print(form.errors)
        # retornar a lista de erros
        # renderiza o formulário mostrando os erros
        return self.render_to_response(self.get_context_data(form=form))
    
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class=ItemForm
    template_name = 'item/edita_item.html'
    success_url = reverse_lazy('item:meus_itens')
    context_object_name = 'item' 
    def form_valid(self,form):
        messages.success(self.request,"Item alterado com sucesso!")
        self.object = form.save()
        return HttpResponse('<script>window.location.reload();</script>')  

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'item/deletar_item.html'
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('item:meus_itens')
    def form_valid(self,form):
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request,"Item deletado com sucesso!")
        return HttpResponseRedirect(success_url)

# MODEL +  Class-Based View = Nome da classe
