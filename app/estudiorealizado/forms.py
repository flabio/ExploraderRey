from django.forms import ModelForm
from app.estudiorealizado.models import EstudioRealizado
from django import forms

class EstudioRealizadoForm(forms.ModelForm):
    class Meta:
        model = EstudioRealizado
        fields = (
            'universitarios',
            'num_semestre',
            'titulo_obtenido',
            'posgrado',
            'teologicos',
            'estado',
            'user',
            )
        labels = {
            'universitarios':'Universitarios',
            'num_semestre':'Número semestre',
            'titulo_obtenido':'Titulo Obtenido',
            'posgrado':'Posgrado',
            'teologicos':'Teologicos',
            'estado':'Estado',
            
        }
        widgets = {
            'universitarios':forms.CheckboxInput(attrs={'class':''}),
            'num_semestre':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'titulo_obtenido':forms.TextInput(attrs={'class':'form-control','value':''}),
            'posgrado':forms.TextInput(attrs={'class':'form-control','value':''}),
            'teologicos':forms.TextInput(attrs={'class':'form-control','value':''}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
        }