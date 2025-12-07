from django import forms
from .models import Reserva, Viaje

class ReservaForm(forms.ModelForm):
   class Meta:
      model = Reserva
      fields = ['nombre', 'email', 'viaje', 'personas']
      widgets = {
         'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
         'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'}),
         'viaje': forms.Select(attrs={'class': 'form-control'}),
         'personas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
      }

