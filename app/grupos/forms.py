"""Grupo form"""
from django import forms
#models
from app.grupos.models import Grupos

class GrupoForm(forms.ModelForm):
    """Grupo model form"""
    class Meta:
        """Form settings"""
        model  = Grupos
        fields = ('nombre','imagen','estado')
        labels = {
            'nombre':'Nombre del Grupo',
            'imagen':'Logo',
            'estado':'Estado',
            
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
           
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
        }