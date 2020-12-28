from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Seccion(models.Model):
    seccion_id  = models.AutoField(primary_key=True)
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    seccion     = models.IntegerField()
    estado      = models.BooleanField(default = True)
    created     = models.DateTimeField(auto_now_add = True)
    modified    = models.DateTimeField(auto_now = True)
    def __str__(self):
        return '{} @ {}'.format(self.seccion_id,self.seccion)