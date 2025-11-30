from django.urls import path
from . import views
from .views import ViajeListView, ViajeDetailView

urlpatterns = [
   path('', views.home, name='Inicio'),

   path('viajes/', views.viajes, name='Viajes'),
   path('actividades/', views.actividades, name='Actividades'),
   path('usuarios/', views.usuarios, name='Usuarios'),
   path('contacto/', views.contacto, name='Contacto'),


   # Listas y detalles

   path('actividades/lista/', views.lista_actividades, name='lista_actividades'),
   path('actividades/<int:pk>/', views.detalle_actividad, name='detalle_actividad'),

   path('usuarios/lista/', views.lista_usuarios, name='lista_usuarios'),
   path('usuarios/<int:pk>/', views.detalle_usuario, name='detalle_usuario'),

   path('filtrar_viajes/', views.filtrar_viajes, name='filtrar_viajes'),


   # Usando vistas basadas en clases

   path('viajes/lista/', ViajeListView.as_view(), name='lista_viajes'),
   path('viajes/<int:pk>/', ViajeDetailView.as_view(), name='detalle_viaje'),


]
