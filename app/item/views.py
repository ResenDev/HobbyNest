from user.models import Usuario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .models import Item
# Create your views here.


@login_required
class ItemListView(ListView):
    model = Item


@login_required
class ItemUpdateView(UpdateView):
    model = Item


@login_required
class ItemCreateView(CreateView):
    model = Item


@login_required
class ItemDeleteView(DeleteView):
    model = Item
# MODEL +  Class-Based View = Nome da classe
