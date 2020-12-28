"""Iglesia form"""
from django import forms

#models
from app.iglesia.models import Iglesia


class IglesiaForm(forms.ModelForm):
    """Iglesia model form """
    class Meta:
        """Form settings."""
        model  = Iglesia
        fields = ('nombre','direccion','telefono','correo','estado')
        labels = {'nombre':'Nombre de la Inglesia','correo':'Email','direccion':'Dirección de la Inglesia','telefono':'Teléfono de la Iglesia',}
        widgets = {
                'nombre':forms.TextInput(attrs={'class':'form-control'}),
                'correo':forms.TextInput(attrs={'class':'form-control'}),
                'direccion':forms.TextInput(attrs={'class':'form-control'}),
                'telefono':forms.TextInput(attrs={'class':'form-control'}),
                'estado':forms.CheckboxInput(attrs={'class':''}),
        }