import csv
import weasyprint
import tempfile
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# é equivalente a um @login_required, mas para CBV.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import CreateView
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponseRedirect, HttpResponse


class MeuPaginator(Paginator):
    def page(self, number):
        try:
            number = self.validate_number(number)
        except InvalidPage:  # engloba PageNotAnInteger e EmptyPage
            number = self.num_pages  # retorna a última página
        return super().page(number)


class ItemListView(LoginRequiredMixin, ListView):
    # template onde será renderizada a lista
    template_name = 'item/lista_itens.html'
    model = Item
    paginator_class = MeuPaginator
    paginate_by = 10  # limite de itens por página
    context_object_name = 'itens'  # nome da lista de objetos que será passada ao html
    # TODO resolver erro das urls

    def get_queryset(self):
        # retorna os itens do usuário logado (que está fazendo o request), ordenado pelo q foi atualizado mais recentemente
        # valor inicial
        qs = Item.objects.order_by(
            '-updated_at').filter(user_FK_id=self.request.user)

        # captura o elemento com name = pesquisa no html
        search = self.request.GET.get('pesquisa')
        if search:
            qs = qs.filter(titulo__icontains=search)

        # captura o valor da variavel que influenciará a ordenação
        ordem = self.request.GET.get("ordenacao")
        if ordem:
            # ordena de acordo com o valor da variável ordenacao
            qs = qs.order_by(ordem)

        return qs


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'item/detalhe_item.html'
    context_object_name = 'item'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/cadastro_item.html'
    success_url = reverse_lazy('item:meus_itens')

    def form_valid(self, form):
        # atribui o usuario logado ao campo user_FK
        form.instance.user_FK = self.request.user
        messages.success(self.request, "Item criado com sucesso!")
        self.object = form.save()  # salva o objeto no banco
        # atualiza a página usando js
        return HttpResponse('<script>window.location.reload();</script>')
 # salva e redireciona para a success_url

    def form_invalid(self, form):
        print(form.errors)
        # retornar a lista de erros via console
        # renderiza o formulário mostrando os erros
        return self.render_to_response(self.get_context_data(form=form))


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/edita_item.html'
    success_url = reverse_lazy('item:meus_itens')
    context_object_name = 'item'

    def form_valid(self, form):
        messages.success(self.request, "Item alterado com sucesso!")
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

    def form_valid(self, form):
        self.object.delete()
        messages.success(self.request, "Item deletado com sucesso!")
        return HttpResponseRedirect(self.success_url)

# MODEL +  Class-Based View = Nome da classe


@login_required
def exportar_csv(request):
    response = HttpResponse(
        content_type='text/csv',  # informa ao navegador que o conteúdo é um csv
        # baixa o arquivo csv nomeando como colecao.csv
        headers={'Cotent-Disposition': 'attachment; filename=colecao.csv'}
    )

    writer = csv.writer(response)  # vai escrever os dados do response como csv
    writer.writerow(['titulo', 'categoria', 'marca',
                    'descricao_item', 'ano_aquisicao'])  # cabeçalho da planilha

    itens = Item.objects.order_by(
        '-updated_at').filter(user_FK_id=request.user)
    for item in itens:
        # escreve uma linha com os dados do item para cada item dentro da lista
        writer.writerow([item.titulo, item.categoria, item.marca,
                        item.descricao_item, item.ano_aquisicao])
    return response


@login_required
def exportar_pdf(request):
    itens = Item.objects.order_by(
        '-updated_at').filter(user_FK_id=request.user)
    tamanho = len(itens)
    html_index = render_to_string(
        'item/pdf_view.html', {'itens': itens, 'tamanho': tamanho})
    weasyprint_html = weasyprint.HTML(
        string=html_index, base_url='http://127.0.0.1:8000/itens/meus_itens/')
    pdf = weasyprint_html.write_pdf(
        stylesheets=[weasyprint.CSS(string='body { font-family: serif }')])
    response = HttpResponse(content_type='application/pdf')
    response['Cotent-Disposition'] = 'attachment; filename=MeusItens.pdf'
    response['Content-Transfer-Encoding'] = 'binary'

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(pdf)
        output.flush()
        output.seek(0)
        response.write(output.read())
    return response
