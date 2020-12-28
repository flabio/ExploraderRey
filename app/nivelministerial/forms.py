"""NivelMinisterial form"""
from django import forms

#models
from app.nivelministerial.models import NivelMinisterial



class NivelMinisterialForm(forms.ModelForm):
    """Nivel Ministerial model form """
    class Meta:
        """Form settings."""
        model  = NivelMinisterial
        fields = ('nombre','lugar','fecha','user','estado')
        labels = {'nombre':'Adiestramiento','lugar':'Lugar','fecha':'Fecha'}
        widgets = {
                'nombre':forms.TextInput(attrs={'class':'form-control'}),
                'lugar':forms.TextInput(attrs={'class':'form-control'}),
                'fecha':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control','type':'date'}),
                'estado':forms.CheckboxInput(attrs={'class':''}),
        }