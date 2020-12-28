# models
from  app.patrulla.models import Patrulla
# formularios
from app.patrulla.forms import PatrullaForm
#Exception
from django.db.utils import IntegrityError
#utilidades
from utilidades.utilidades import  Utilidades

from .patrulla_serializer import  patrulla_serializer

class patrulla_repository:

    def listado_patrulla(self,*args, **kwargs):
        try:
            datos=[]
            listado = Patrulla.objects.filter()
        
            for item in listado:
                dict_patrulla = {
                    'pk':item.pk,
                    'nombre':item.nombre,
                    'imagen':str(item.imagen),
                    'grupo':item.grupo.nombre,
                    'grupo_id':item.grupo_id,
                    'estado':item.estado,
                    'created':str(item.created)
                }
                datos.append(dict_patrulla)
            return datos
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    
    def crear_patrulla(self,request,*args,**kwargs):
        try:
            if request.method=='POST':
                form=PatrullaForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return Utilidades.get_messages_200(self)
                else:
                    return Utilidades.get_messages_400(self,'Error, el nombre ya existe.')    
               
            else:
                PatrullaForm()
                return Utilidades.get_messages_400(self,'La pertición de http debe ser post')
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))

    def editar_patrulla(self,request,pk,*args,**kwagrs):
        try:
            patrulla = Patrulla.objects.get(pk=pk)
            if len(request.FILES)>0:
                patrulla.imagen = request.FILES['imagen']
            patrulla.nombre = request.POST.get('nombre')
            patrulla.grupo_id = request.POST.get('grupo')
            patrulla.estado = Utilidades.validar_estado(self,request.POST.get('estado'))
            patrulla.save()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    
    def eliminar_patrulla(self,pk,*args,**kwagrs):
        try:
            patrulla = Patrulla.objects.get(pk=pk)
            patrulla.delete()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    
    # def validar_codigo(self,codigo):
    #     return Patrulla.objects.filter(codigo=codigo).count()
        

