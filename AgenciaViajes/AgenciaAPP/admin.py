from django.contrib import admin
from .models import Usuario, Viaje, Actividad

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Viaje)
admin.site.register(Actividad)