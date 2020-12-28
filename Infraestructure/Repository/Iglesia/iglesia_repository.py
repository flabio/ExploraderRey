from  app.iglesia.models import Iglesia
from django.db.utils import IntegrityError
from utilidades.utilidades import Utilidades
# forms
from app.iglesia.forms import  IglesiaForm
# Create your views here.

class iglesia_repository:

    def listado_iglsia(self,*args, **kwargs):
        try:
            result = Iglesia.objects.filter()
            return [{
                    'iglesia_id':item.pk,
                    'nombre':item.nombre,
                    'direccion':item.direccion,
                    'telefono':item.telefono,
                    'correo':item.correo,
                    'estado':item.estado,
                    'created':str(item.created)
                } for item in result]
        
        except IntegrityError as error:
            return Utilidades.get_messages_400(self,'No existe datos.'+str(error.args[1]))
 
    def create_iglesia(self,request,*args,**kwargs):
        try:
            
            form = IglesiaForm(request.POST)
            if form.is_valid():
                form.save()
                return Utilidades.get_messages_200(self)
            else:
                return Utilidades.get_messages_400(self,'no se puede registrar la datos.')
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))

    def get_editar_iglesia(self,request,pk,*args,**kwargs):
        try:
            iglesia = Iglesia.objects.get(pk=pk)
            iglesia.nombre    = request.POST.get('nombre')
            iglesia.direccion =   request.POST.get('direccion')
            iglesia.telefono  =   request.POST.get('telefono')
            iglesia.correo    =   request.POST.get('correo')
            iglesia.estado    =   Utilidades.validar_estado(self,request.POST.get('estado'))
            iglesia.save()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))

    def eliminar_iglesia(self,pk,*args,**kwargs):
        try:
            object = Iglesia.objects.get(pk=pk)
            object.delete()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
