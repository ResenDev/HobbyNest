from django import forms
from .models import Item
# cadastro e modificação de itens

class ItemForm(forms.ModelForm):
    class  Meta:
        model = Item
        fields = ['titulo','marca','descricao_item','categoria',
                  'ano_aquisicao']