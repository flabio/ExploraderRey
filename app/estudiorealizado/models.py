from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EstudioRealizado(models.Model):
    universidad_id      = models.AutoField(primary_key=True)
    user                = models.ForeignKey(User,on_delete=models.CASCADE)
    universitarios      = models.BooleanField(default = True)
    num_semestre        = models.CharField(max_length = 50, blank = False, null = False)
    titulo_obtenido     = models.TextField()
    posgrado            = models.TextField()
    teologicos          = models.TextField()
    estado              = models.BooleanField(default = True)
    created             = models.DateTimeField(auto_now_add = True)
    modified            = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '{}'.format(self.estudiorealizado_id)
