from django import forms
from .models import Item
# cadastro e modificação de itens


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['user_FK']  # Exclui o campo user_FK do formulário
        # capos do formulário
        fields = ['titulo', 'marca', 'descricao_item', 'categoria',
                  'ano_aquisicao']
        widgets = {  # substituindo o input do bootstrap direto no formulário
            'categoria': forms.Select(attrs={
                'class': 'form-select',
                'id': 'floatingSelect',
                'aria-label': 'Floating label select example'
            }),
        }
        
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            raise forms.ValidationError("O título é obrigatório.")
        return titulo  #campo

    def clean_marca(self):
        marca = self.cleaned_data.get('marca')
        # Adicione validações se necessário
        return marca  # Retorne o valor

    def clean_descricao_item(self):
        descricao = self.cleaned_data.get('descricao_item')
        # Adicione validações se necessário
        return descricao  # Retorne o valor

    def clean_ano_aquisicao(self):
        ano = self.cleaned_data.get('ano_aquisicao')
        # Adicione validações se necessário
        return ano  # Retorne o valor