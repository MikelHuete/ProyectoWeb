from django.contrib import admin
from .models import Usuario, Viaje, Actividad, Reserva
from django.contrib.auth.models import Group

# Registrar Usuario para superusuarios
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro')


# Registrar Viaje con control de permisos por grupo
@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('destino', 'fecha_inicio', 'fecha_fin', 'precio')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Solo los superusuarios ven todo
        if request.user.is_superuser:
            return qs
        # Usuarios del grupo 'Gestor de viajes' solo ven viajes
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return qs
        return qs.none()

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return True
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False  # Opcional: no permitimos borrar


# Registrar Actividad con control de permisos
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_viaje', 'horario')

    def get_viaje(self, obj):
        return ", ".join([v.destino for v in obj.viaje.all()])
    get_viaje.short_description = 'Viaje'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return qs
        return qs.none()

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return True
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'viaje', 'personas', 'fecha_reserva')
    list_filter = ('viaje', 'fecha_reserva')
    search_fields = ('nombre', 'email', 'viaje__destino')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return qs
        return qs.none()

    def has_change_permission(self, request, obj=None):
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return True
        return super().has_change_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.groups.filter(name='Gestor de viajes').exists():
            return True
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Solo superusuarios pueden borrar