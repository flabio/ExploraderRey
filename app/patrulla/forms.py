"""Grupo form"""
from django import forms
#models
from app.patrulla.models import Patrulla

class PatrullaForm(forms.ModelForm):
    """Patrulla model form"""
    class Meta:
        """Form settings"""
        model  = Patrulla
        fields = ('nombre','grupo','imagen','estado')
        labels = {
            'nombre':'Nombre del Grupo',
            'imagen':'Logo',
            'gurpo':'Grupo',
            'estado':'Estado',
            
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
           
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
        }