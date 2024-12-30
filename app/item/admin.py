# users/admin.py
from django.contrib import admin
from item.models import Item


@admin.register(Item)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id','titulo','categoria','marca','descricao_item','ano_aquisicao','user_FK'
    ordering='id',