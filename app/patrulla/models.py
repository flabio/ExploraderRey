from django.db import models
from django.contrib.auth.models import User
from app.grupos.models import Grupos
# local


# Create your models here.
class Patrulla(models.Model):
    patrulla_id             = models.AutoField(primary_key = True, auto_created = True)
    grupo                   = models.ForeignKey(Grupos,on_delete=models.CASCADE)
    nombre                  = models.CharField(max_length = 150, blank = False, null = False,unique=True)
    imagen                  = models.ImageField(upload_to='grupo/imagenes',blank=True, null=True)
    #codigo                  = models.CharField(max_length = 150, blank = True, null = True)
    estado                  = models.BooleanField(default = True)
    created                 = models.DateTimeField(auto_now_add = True)
    modified                = models.DateTimeField(auto_now = True)


    def __str__(self):
        return '{} @ {}'.format(self.patrulla_id,self.nombre)

