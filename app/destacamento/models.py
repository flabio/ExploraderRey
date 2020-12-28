from django.db import models
from django.contrib.auth.models import User
# local
from app.iglesia.models import Iglesia
from app.seccion.models import Seccion

# Create your models here.
class Destacamento(models.Model):
    destacamento_id     = models.AutoField(primary_key = True, auto_created = True)
    iglesia             = models.ForeignKey(Iglesia,on_delete=models.CASCADE)
    seccion             = models.ForeignKey(Seccion,on_delete=models.CASCADE)
    nombre              = models.CharField(max_length = 250, blank = False, null = False)
    imagen              = models.ImageField(upload_to='destacamento/imagenes',blank=True, null=True)
    distrito            = models.CharField(max_length = 250, blank = False, null = False)
    numero              = models.IntegerField(unique=True)
    estado              = models.BooleanField(default = True)
    created             = models.DateTimeField(auto_now_add = True)
    modified            = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} @ {}'.format(self.destacamento_id,self.nombre)

