from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.users.models import Perfil
from app.estudiorealizado.models import EstudioRealizado
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password1','password2','is_superuser','is_staff','is_active']
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Email',
            'username':'Usuario',
            'password1':'Contraseña',
            'password2':'Confirmación de Contraseña',
            'is_superuser':'Estado de superusuario',
            'is_staff':'Estado del personal',
            'is_active':'Activo',
        }
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control','type':'email'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','type':'password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','type':'password'}),
            'is_superuser':forms.CheckboxInput(attrs={'class':'form-control'}),
            'is_staff':forms.CheckboxInput(attrs={'class':''}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }

class PerfilFrom(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = (
            'user',
            'foto',
            'identificacion',
            'tipo_identificacion',
            'fecha_nacimiento',
            'lugar_nacimiento',
            'genero',
            'tipo_sangre',
            'direccion',
            'telefono',
            'celular',
            'profesion',
            'estado_civil',
            'eps',
            'anion_conversion',
            'bautismo_agua',
            'bautismo_espiritu',
            'primaria',
            'secundarias',
            'primaria_anio_cursado',
            'segundaria_anio_cursado',
            'estado',
            
            )
        labels = {
            'user':'Usuario',
            'foto':'Foto',
            'identificacion':'Identificación',
            'tipo_identificacion':'Tipo Identificación',
            'fecha_nacimiento':'Fecha Nacimiento',
            'lugar_nacimiento':'Lugar Nacimiento',
            'genero':'Genero',
            'tipo_sangre':'Tipo Sangre',
            'direccion':'Dirección',
            'telefono':'Teléfono',
            'celular':'Celular',
            'profesion':'Profesión',
            'estado_civil':'Estado Civil',
            'eps':'Eps',
            'anion_conversion':'Año Conversión',
            'bautismo_agua':'Bautismo Agua',
            'bautismo_espiritu':'Bautismo Espiritu',
            'estado':'Estado',
            'primaria':'Primaria',
            'secundarias':'Segundaria',
            'primaria_anio_cursado':'Años cursados',
            'segundaria_anio_cursado':'Años cursados'
        }
        widgets = {
            'foto':forms.FileInput(attrs={'class':'form-control'}),
            'identificacion':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'tipo_identificacion':forms.Select(attrs={'class':'form-control'}),
            'fecha_nacimiento':forms.DateInput(format='%Y-%m-%d',attrs={'class':'form-control','type':'date'}),
            'lugar_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
            'genero':forms.Select(attrs={'class':'form-control select2'}),
            'tipo_sangre':forms.Select(attrs={'class':'form-control select2'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'celular':forms.TextInput(attrs={'class':'form-control'}),
            'profesion':forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil':forms.Select(attrs={'class':'form-control select2'}),
            'eps':forms.Select(attrs={'class':'form-control select2'}),
            'anion_conversion':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'bautismo_agua':forms.CheckboxInput(attrs={'class':''}),
            'bautismo_espiritu':forms.CheckboxInput(attrs={'class':''}),
            'estado':forms.CheckboxInput(attrs={'class':''}),
            'primaria':forms.CheckboxInput(attrs={'class':''}),
            'secundarias':forms.CheckboxInput(attrs={'class':''}),
            'primaria_anio_cursado':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'segundaria_anio_cursado':forms.TextInput(attrs={'class':'form-control','type':'number'}),
        }

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