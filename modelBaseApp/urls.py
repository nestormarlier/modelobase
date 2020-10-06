from django.urls import path
from .views import inicio, categoria, fichatecnica

urlpatterns = [
    path('home/', inicio, name='Home'),
    path('categorias/', categoria, name='Categorias'),
    path('fichastecnicas/', fichatecnica, name='Categorias'),
]