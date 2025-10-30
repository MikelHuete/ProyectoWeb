from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
   return HttpResponse('Inicio de la Agencia de Viajes')

def viajes(request):
   return HttpResponse('Página de gestión de viajes')

def actividades(request):
   return HttpResponse('Página de gestión de actividades')

def usuarios(request):
   return HttpResponse('Página de gestión de usuarios')
