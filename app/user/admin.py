# users/admin.py
from django.contrib import admin
from user.models import Usuario


@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','username','email','is_staff',
    ordering='id',