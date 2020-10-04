from django.shortcuts import render

from .models import Categoria, FichaTecnica

# Create your views here.


def inicio(request):
    data = {
        'title': 'Página de inicio'
    }
    return render(request, 'base.html', data)

def categoria(request):
    data = {
        'title': 'Listado de categorías',
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'categorias/list.html', data)

def fichatecnica(request):
    data = {
        'title':'Fichas Técnicas',
        'fichastecnicas': FichaTecnica.objects.all()
        }
    return render(request,'fichastecnicas/list.html', data)