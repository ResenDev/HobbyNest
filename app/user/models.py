from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Usuario(AbstractUser):
    # sobrescrever o fato do nome e email virem blank por padrão
    first_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)
    