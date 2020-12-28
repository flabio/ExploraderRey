"""Grupo form"""
from django import forms
#models
from app.eps.models import Eps

class EpsForm(forms.ModelForm):
    """Eps model form"""
    class Meta:
        """Form settings"""
        model  = Eps
        fields = ('nombre','estado')
        labels = {
            'nombre':'Nombre del Eps',
            'estado':'Estado',
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
        }