from django.urls import path
from .views import inicio, categoria

urlpatterns = [
    path('home/', inicio, name='Home'),
    path('categorias/', categoria, name='Categorias'),
]
