from django.shortcuts import render

from .models import Categoria

# Create your views here.


def inicio(request):
    data = {
        'title': 'Página de inicio'
    }
    return render(request, 'index.html', data)

def categoria(request):
    data = {
        'title': 'Listado de categorías',
        'categorias': Categoria.objects.all(),
    }
    return render(request, 'categorias/list.html', data)
