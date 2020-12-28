from  app.eps.models import Eps
from app.eps.forms import EpsForm
from  utilidades.utilidades import Utilidades
from django.db.utils import IntegrityError
# from django.core import serializers
# from rest_framework import  serializers
# from .eps_serializer import eps_serializer
import json
class  eps_reposity:

    def listado_eps(self,*args,**kwargs):
        try:
            eps = Eps.objects.all().order_by('-created')
            return [{'eps_id':item.pk,
                    'nombre':item.nombre.capitalize(),
                    'estado':item.estado,
                    'created':str(item.created)} for item in eps]
            
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,'Error de services '+str(error.args[0]))
    
    def crear_eps(self,request,*args,**kwargs):
        try:
            form = EpsForm(request.POST)
            if form.is_valid():
                form.save()
                return Utilidades.get_messages_200(self,'El registro se guardo exitosamente.')
            else:
                return Utilidades.get_messages_400(self,'El datos no se pueden guardar por favor valide.')
            
        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,'Error de services '+str(error.args[0]))
    
    def editar_eps(self,request,pk):
        try:
            eps = Eps.objects.get(pk=pk)
            eps.nombre = request.POST.get('nombre')
            eps.estado = Utilidades.validar_estado(self,request.POST.get('estado'))
            eps.save()
            return Utilidades.get_messages_200(self,'El registro se actualizo exitosamente.')
        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,'Error de services '+str(error.args[0]))
    def eliminar_eps(self,pk):
       try:
           eps=Eps.objects.get(pk=pk)
           eps.delete()
           return Utilidades.get_messages_200(self,'The record was successfully deleted')
       except IntegrityError as error:
           return Utilidades.get_messages_500(self,'Error de services '+str(error.args[0]))

    
    def validar_nombre_existe(self,nombre):
        return Eps.objects.filter(nombre=nombre).count()        