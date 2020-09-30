from django.shortcuts import render

# Create your views here.

def inicio(request):
    data = {
        'title': 'Página de inicio'
    }
    return render(request, 'index.html',data)