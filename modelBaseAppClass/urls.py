from django.urls import path
from .views import CategoriaListView, FichaTecnicaListView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='Categorias'),
    path('fichastecnicas/', FichaTecnicaListView.as_view(), name='FichasTecnicas'),
]