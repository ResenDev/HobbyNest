from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    # sobrescrever o fato do nome e email virem blank por padrão
    first_name = models.CharField(
        max_length=30,
        blank=False
    )
    email = models.EmailField(
        null=False,
        blank=False,
        unique=True
    )

    