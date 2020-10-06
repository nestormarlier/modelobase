from django.shortcuts import render

from modelBaseApp.models import Categoria

from django.views.generic.list import ListView
# Create your views here.

class CategoriasListView(ListView):
    model = Categoria
    template_name = "datatable/categorias/list.html"
    
    def get_queryset(self):
        return super().get_queryset()
        
        return context