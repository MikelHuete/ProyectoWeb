from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='Inicio'),

   # Rutas para la gestión de viajes
   # 127.0.0.1:8000/AgenciaAPP/viajes/
   path('viajes/', views.viajes, name='Viajes'),

   path('actividades/', views.actividades, name='Actividades'),

   path('usuarios/', views.usuarios, name='Usuarios'),
]
