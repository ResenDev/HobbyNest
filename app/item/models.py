from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Item(models.Model):
    class Categoria(models.TextChoices):
        LIVRO = 'Livro'
        JOGO = 'Jogo'
        FILME_OU_SERIE = 'Filme/Série'
        ACTION_FIGURE = 'Action Figure'

    user_FK = models.ForeignKey(
        settings.AUTH_USER_MODEL,# referencia ao  modelo definido no settings.py (Usuario)
        on_delete=models.CASCADE,
        related_name='itens' # permite que eu busque os itens pelo user_FK ex: user_FK.itens.all()
    )
    titulo = models.CharField(
        max_length=100,
        blank=False,
    )
    marca = models.CharField(
        max_length=100,
        blank=False,
    )
    descricao_item = models.TextField(
        blank=True,
        null= True,
        max_length=500
    )
    categoria = models.CharField(
        max_length=50,
        choices=Categoria.choices,  # as opções estão definidas na classe Categoria
        default=Categoria.LIVRO,
        blank=False,
    )
    ano_aquisicao = models.IntegerField(
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
    )
    updated_at = models.DateTimeField( #muda sempre q o obj for alterado
        auto_now=True
    )

    def __str__(self):
        return self.titulo
