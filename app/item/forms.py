from django import forms
from django.forms import ModelForm
from .models import Item
# cadastro e modificação de itens

class ItemForm(ModelForm):
    class  Meta:
        model = Item
        fields = ('titulo','marca','descricao_item','categoria',
                  'ano_aquisicao')