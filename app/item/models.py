from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
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
        settings.AUTH_USER_MODEL,#  referencia ao  modelo definido no settings.py (Usuario)
        on_delete=models.CASCADE,
        related_name='itens' # permite que eu busque os itens pelo user_FK ex: user_FK.itens.all()
    )
    titulo = models.CharField(
        max_length=255,
        blank=False,
    )
    marca = models.CharField(
        max_length=255,
        blank=False,
    )
    descricao_item = models.TextField(
        blank=True,
        null= True
    )
    categoria = models.CharField(
        max_length=50,
        choices=Categoria.choices,  # as opções estão definidas na classe Categoria
        default=Categoria.LIVRO,
        blank=False,
    )
    ano_aquisicao = models.IntegerField(
        validators=[
            MinValueValidator(1950),  # ano mínimo
            MaxValueValidator(datetime.now().year)  # ano atual é o limite
        ],
        blank=False,
        help_text="Informe o ano da aquisição do item (ex.: 2018)"
    )
    data_criacao = models.DateTimeField(
        default=timezone.now
    )
    
    def __str__(self):
        return self.titulo
