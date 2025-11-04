from django.db import models

# Create your models here.

class Usuario(models.Model):
   nombre = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   telefono = models.IntegerField(max_length=15, blank=True, null=True)
   fecha_registro = models.DateField(auto_now_add=True)

   def __str__(self):
      return self.nombre


class Viaje(models.Model):
   destino = models.CharField(max_length=150)
   descripcion = models.TextField()
   fecha_inicio = models.DateField()
   fecha_fin = models.DateField()
   precio = models.DecimalField(max_digits=8, decimal_places=2)
   usuario = models.ManyToManyField(Usuario, related_name='viajes')

   def __str__(self):
      return f"{self.destino} ({self.fecha_inicio} - {self.fecha_fin})"


class Actividad(models.Model):
   nombre = models.CharField(max_length=100)
   descripcion = models.TextField(blank=True, null=True)
   horario = models.TimeField(blank=True, null=True)
   viaje = models.ManyToManyField(Viaje, related_name='actividades')

   def __str__(self):
      return f"{self.nombre} - {self.viaje.first().destino}"