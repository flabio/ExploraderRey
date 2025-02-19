from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NivelMinisterial(models.Model):
    nivelministerial_id = models.AutoField(primary_key=True)
    nombre              = models.TextField()
    lugar               = models.TextField()
    fecha               = models.DateField(auto_now = False)
    user                = models.ForeignKey(User,on_delete=models.CASCADE,blank=False, null=False)
    estado              = models.BooleanField(default = True)
    created             = models.DateTimeField(auto_now_add = True)
    modified            = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} @ {}'.format(self.nivelministerial_id,self.nombre)