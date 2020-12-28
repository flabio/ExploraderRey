from django.db import models

# Create your models here.
class Eps(models.Model):
    eps_id      = models.AutoField(primary_key = True)
    nombre      = models.CharField(max_length = 250, blank = False, null = False)
    estado      = models.BooleanField(default = True)
    created     = models.DateTimeField(auto_now_add = True)
    modified    = models.DateTimeField(auto_now = True)
    def __str__(self):
        return '{}'.format(self.nombre)