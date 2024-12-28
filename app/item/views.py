from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
# Create your views here.
@login_required
class  ItemListView(ListView):
    ...
@login_required
class  ItemUpdateView(UpdateView):
    ...
@login_required
class  ItemCreateView(CreateView):
    ...
@login_required
class  ItemDeleteView(DeleteView):
    ...
# MODEL +  Class-Based View = Nome da classe
