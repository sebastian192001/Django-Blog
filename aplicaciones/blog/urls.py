from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name = 'index'),
    path('generales/',generales, name = 'generales'),
    path('programacion/',programacion, name = 'programacion'),
    path('videojuegos/',videojuegos, name = 'videojuegos'),
    path('tecnologia/',tecnologia, name = 'tecnologia'),
    path('tutoriales/',tutoriales, name = 'tutoriales'),
    path('<slug:slug>',detallePost, name = 'detalle_post'),
]