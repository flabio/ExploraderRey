from django.db import models
from django.contrib.auth.models import User
from app.eps.models import Eps
from app.destacamento.models import Destacamento
# Create your models here.
class Perfil(models.Model):
    GENERO_CHOICES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer')
    ]
    TIPO_IDEN_CHOICES = [
        ('Cc', 'Cc'),
        ('Ti', 'Ti'),
        ('Rc', 'Rc'),
        ('Otros', 'Otros'),
    ]
    TIPO_SANGRE_CHOICES=[
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
    ]
    ESTADO_CIVIL_CHOICES=[
        ('Casado(a)', 'Casado(a)'),
        ('Soltero(a)', 'Soltero(a)'),
        ('Viudo(a)', 'Viudo(a)'),
        ('Separado(a)', 'Separado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
    ]
    perfil_id                 = models.AutoField(primary_key=True)
    user                      = models.ForeignKey(User,on_delete=models.CASCADE,blank=False, null=False)
    eps                       = models.ForeignKey(Eps,on_delete=models.CASCADE,blank=False, null=False)
    Destacamento              = models.ForeignKey(Destacamento,on_delete=models.CASCADE,blank = True, null = True)
    foto                      = models.ImageField(upload_to='perfil/imagenes',blank=True, null=True)
    identificacion            = models.CharField(max_length=100,blank=True, null = True, unique = False)
    tipo_identificacion       = models.CharField(max_length = 10, choices = TIPO_IDEN_CHOICES, blank = False, null = False)
    fecha_nacimiento          = models.DateField('Fecha Nacimiento', auto_now = False)
    lugar_nacimiento          = models.CharField(max_length=250,blank= False , null = False)
    genero                    = models.CharField(max_length=10,choices=GENERO_CHOICES, blank = False, null = False)
    tipo_sangre               = models.CharField(max_length=3,choices=TIPO_SANGRE_CHOICES,blank = False, null = False)
    direccion                 = models.CharField(max_length = 100, blank =False, null = False)
    telefono                  = models.CharField(max_length = 100, blank = False, null = False)
    celular                   = models.CharField(max_length = 100, blank = False, null = False)
    profesion                 = models.CharField(max_length = 200, blank = True, null = True)
    estado_civil              = models.CharField(max_length = 50 ,choices = ESTADO_CIVIL_CHOICES,blank = True, null = True)
    anion_conversion          = models.CharField(max_length = 10, blank = True, null = True)
    bautismo_agua             = models.BooleanField(default = True)
    bautismo_espiritu         = models.BooleanField(default = True)
    primaria                  = models.BooleanField(default = True)
    primaria_anio_cursado     = models.IntegerField()
    secundarias                = models.BooleanField(default = True)
    segundaria_anio_cursado   = models.IntegerField()
    estado                    = models.BooleanField(default = True)
    created                   = models.DateTimeField(auto_now_add = True)
    modified                  = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(self.perfil_id)
