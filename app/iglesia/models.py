from django.db import models

# Create your models here.
class Iglesia(models.Model):
    iglesia_id  = models.AutoField(primary_key = True, auto_created = True)
    nombre      = models.CharField(max_length = 250, blank = False, null = False,unique = False)
    direccion   = models.CharField(max_length = 250, blank = False, null = False)
    telefono    = models.CharField(max_length = 250, blank = False, null = False)
    correo      = models.EmailField(unique = False, max_length = 250, blank = False, null = False)
    estado      = models.BooleanField(default = True)
   # imagen      = models.ImageField(upload_to='grupo/imagenes',blank=True, null=True)
    created     = models.DateTimeField(auto_now_add = True)
    modified    = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{} @ {}'.format(self.iglesia_id,self.nombre)
