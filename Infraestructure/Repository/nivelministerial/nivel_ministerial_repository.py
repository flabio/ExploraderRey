from  app.nivelministerial.models import NivelMinisterial
from app.nivelministerial.forms import NivelMinisterialForm
from django.db.utils import IntegrityError
from utilidades.utilidades import Utilidades

# Create your views here.

class nivel_ministerial_repository:

    def crear_nivel_ministerial(self,request,*args,**kwargs):
        try:

            form = NivelMinisterialForm(request.POST)
            if form.is_valid():
                form.save()
                return Utilidades.get_messages_200(self)
            else:
                return Utilidades.get_messages_400(self,'El datos no se pueden guardar por favor valide.')

        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
    def eliminar_nivel_ministerial(self,pk):
        try:
            nivel_ministerial=NivelMinisterial.objects.filter(pk=pk)
            nivel_ministerial.delete()
            return Utilidades.get_messages_200(self)

        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    def listado_nivel_ministerial(self,pk,*args,**kwargs):
        try:
            return [{'pk':item.pk,
                        'nombre':item.nombre,
                        'lugar':item.lugar,
                        'fecha':str(item.fecha),
                        'estado':item.estado}
                        for item in NivelMinisterial.objects.filter(user_id=pk).order_by('created')]
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
    def get_nivel_ministerial(self,pk,*args, **kwargs):
        try:
            return NivelMinisterial.objects.filter(user_id=pk)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
 
      
