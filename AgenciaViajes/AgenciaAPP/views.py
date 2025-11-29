from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from AgenciaAPP.models import Actividad, Usuario, Viaje

# Create your views here.
def home(request):
   destinos = Viaje.objects.values_list('destino', flat=True).distinct()
   return render(request, 'index.html', {'destinos': destinos})

def viajes(request):
   return render(request, 'viajes/Viajes.html')

def actividades(request):
   return render(request, 'actividades/Actividades.html')

def usuarios(request):
   return render(request, 'usuarios/Usuarios.html')

def contacto(request):
    return render(request, 'contacto.html')

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

def filtrar_viajes(request):
   print("Llegó una petición Ajax")  # Esto aparece en la consola donde corres `runserver`

   destino = request.GET.get('destino', '')
   fecha_inicio = request.GET.get('fecha_inicio', '')
   fecha_fin = request.GET.get('fecha_fin', '')

   print(f"Destino: {destino}, Fecha inicio: {fecha_inicio}, Fecha fin: {fecha_fin}")

   viajes = Viaje.objects.all()

   if destino and destino != "Destinos":
      viajes = viajes.filter(destino__icontains=destino.strip())

   if fecha_inicio:
      viajes = viajes.filter(fecha_inicio__gte=fecha_inicio)
   if fecha_fin:
      viajes = viajes.filter(fecha_fin__lte=fecha_fin)

   if destino:
      viajes = viajes.filter(destino__icontains=destino)

   return render(request, "viajes/resultados_viajes.html", {"viajes": viajes})



