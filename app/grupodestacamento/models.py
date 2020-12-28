from django.db import models
from app.destacamento.models import Destacamento
from app.grupos.models import Grupos
# Create your models here.
class GrupoDestacamento(models.Model):
    grupodestacamento_id    =  models.AutoField(primary_key = True, auto_created = True)
    dgrupo                  = models.ForeignKey(Grupos,on_delete=models.CASCADE)
    destacamento            = models.ForeignKey(Destacamento,on_delete=models.CASCADE)
    created                 = models.DateTimeField(auto_now_add = True)
    modified                = models.DateTimeField(auto_now = True)
    def __str__(self):
      return '{}'.format(self.grupodestacamento_id)