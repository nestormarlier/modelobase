from django.urls import path
from .views import inicio

urlpatterns = [
    path('home/', inicio, name='Home'),
]
