from django.urls import path
from .views import CategoriasListView

urlpatterns = [
    path('categorias/', CategoriasListView.as_view(), name='CategoriasDataTable'),
]