from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from AgenciaAPP.models import Actividad, Usuario, Viaje

# Create your views here.
def home(request):
   return render(request, 'index.html')

def viajes(request):
   return render(request, 'viajes/index.html')

def actividades(request):
   return render(request, 'actividades/index.html')

def usuarios(request):
   return render(request, 'usuarios/index.html')

def lista_viajes(request):
   viajes = Viaje.objects.all()
   context = {'viajes': viajes}
   return render(request, 'viajes/lista_viajes.html', context)

def detalle_viaje(request, pk):
   viaje = get_object_or_404(Viaje, id=pk)
   context = {'viaje': viaje}
   return render(request, 'viajes/detalle_viaje.html', context)

def lista_actividades(request):
   actividades = Actividad.objects.all()
   context = {'actividades': actividades}
   return render(request, 'actividades/lista_actividades.html', context)

def detalle_actividad(request, pk):
   actividad = get_object_or_404(Actividad, id=pk)
   context = {'actividad': actividad}
   return render(request, 'actividades/detalle_actividad.html', context)

def lista_usuarios(request):
   usuarios = Usuario.objects.all()
   context = {'usuarios': usuarios}
   return render(request, 'usuarios/lista_usuarios.html', context)

def detalle_usuario(request, pk):
   usuario = get_object_or_404(Usuario, id=pk)
   context = {'usuario': usuario}
   return render(request, 'usuarios/detalle_usuario.html', context)
