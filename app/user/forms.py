# from django import forms
# from .models import Usuario

# class UsuarioForm(forms.ModelForm):
    
#     username = forms.CharField(
#          max_length=150,
#          required= True,
#          validators=[]
#     )
#     password = forms.CharField(
#          max_length=128,
#          required= True,  
#     )

#     class Meta:
#         model = Usuario
#         fields = ['username','password']

    
#     def clean_username(self):
#         # recebe dado do formulário
#         username = self.cleaned_data['username']
#         # *A Fazer* verifica se o usuario informado existe no banco
#         if not Usuario.objects.filter(username=username).exists():
#             raise forms.ValidationError("Usuário não encontrado.")  
#         return username    
    
#     # def clean_password(self,username):
#     #     username = self.cleaned_data['username']
#     #     senha = self.cleaned_data['password']
#     #     #verifica se existe
#     #     return super().clean()
