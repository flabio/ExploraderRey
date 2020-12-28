"""Grupo form"""
from django import forms
#models
from app.seccion.models import Seccion

class SeccionForm(forms.ModelForm):
    """Seccion model form"""
    class Meta:
        """Form settings"""
        model  = Seccion
        fields = ('seccion','user','estado')
        labels = {
            'nombre':'Nombre del Sección',
            'user':'Usuario',
            'estado':'Estado',
            
        }
        widgets = {
            'seccion':forms.TextInput(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
        }