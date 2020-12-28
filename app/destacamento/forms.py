"""Destacamento form"""
from django import forms
#models
from app.destacamento.models import Destacamento
from app.grupodestacamento.models import GrupoDestacamento

class DestacamentoForm(forms.ModelForm):
    """Destacamento model form"""
    class Meta:
        """Form settings"""
        model  = Destacamento
        fields = ('nombre','iglesia','distrito','numero','seccion','imagen','estado')
        labels = {
            'nombre':'Nombre Destacamento',
            'distrito':'Dristito',
            'iglesia':'Iglesia',
            'numero':'Número',
            'seccion':'Sección',
            'imagen':'Logo',
            'estado':'Estado'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'distrito':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.NumberInput(attrs={'class':'form-control'}),
            'seccion':forms.TextInput(attrs={'class':'form-control'}),
            'iglesia':forms.TextInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
        }


class GrupoDestacamentoForm(forms.ModelForm):
    """Grupo Destacamento model form"""
    class Meta:
        """Form settings"""
        model  = GrupoDestacamento
        fields = ('destacamento','dgrupo')
       