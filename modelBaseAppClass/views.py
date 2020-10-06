from django.shortcuts import render

from django.views.generic.list import ListView

from modelBaseApp.models import Categoria, FichaTecnica

# Create your views here.


class CategoriaListView(ListView):
    model = Categoria
    template_name = "class/categorias/list.html"

    def get_queryset(self):
        return super().get_queryset()
    
        return context


class FichaTecnicaListView(ListView):
    model = FichaTecnica
    template_name = "class/fichastecnicas/list.html"

    def get_queryset(self):
        return super().get_queryset()
        
        return context

