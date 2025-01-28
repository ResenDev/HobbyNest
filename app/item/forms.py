from django import forms
from .models import Item
from datetime import date
# cadastro e modificação de itens


class ItemForm(forms.ModelForm):
    #limitar a inserção de dados por campo
    titulo = forms.CharField(
        max_length=100,
        required=True,
        # substituindo o input do bootstrap direto no formulário
        widget=forms.TextInput(attrs={ 
                'class':'form-control',
                'id':'floatingInput',
                'placeholder':''
                }),
    )
    marca = forms.CharField(
        max_length=100,
        required=True ,
        widget =forms.TextInput(attrs={
                    'class':'form-control',
                    'id':'floatingInput',
                    'placeholder':''
                    }),
        )


    descricao_item = forms.CharField(
        max_length=500,
        required=True ,
        widget =forms.Textarea(attrs={
                    'class':'form-control',
                    'id':'floatingInput',
                    'placeholder':'',
                    'style':'height:100px'
                    }),
        )
    ano_aquisicao = forms.CharField(
        max_length=100,
        required=True ,
        widget =forms.NumberInput(attrs={
                    'class':'form-control',
                    'id':'floatingInput',
                    'placeholder':''
                    }),
        )
    class Meta:
        model = Item
        exclude = ['user_FK']  # Exclui o campo user_FK do formulário
        # campos do formulário
        fields = ['titulo', 'marca', 'descricao_item', 'categoria',
                  'ano_aquisicao']
        widgets = {  
            'categoria': forms.Select(attrs={
                'class': 'form-select',
                'id': 'floatingSelect',
            }),
        }
        
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if titulo[0].islower():
            raise forms.ValidationError("O título deve começar com letra maiúscula.")
        elif len(titulo)>100:
            raise  forms.ValidationError("O campo excedeu o limite de caracteres.")    
        return titulo  # Retorne o valor  para o formulário

    def clean_marca(self):
        marca = self.cleaned_data['marca']
        if len(marca)>100:
            raise  forms.ValidationError("O campo excedeu o limite de caracteres.")    
        return marca 

    def clean_descricao_item(self):
        descricao = self.cleaned_data['descricao_item']
        if len(descricao)>500:
            raise  forms.ValidationError("Descrição muito longa.")    
        return descricao 

    def clean_ano_aquisicao(self):
        ano = self.cleaned_data['ano_aquisicao']
        a  = int(ano)
        data_atual = date.today()
        ano_atual= data_atual.year
        if not 1950 <= a  <= ano_atual  : # verifica se está entre os anos
            raise  forms.ValidationError(f"O ano deve estar no intervalo entre 1950 e {ano_atual}.")    
        return a
            
        
         