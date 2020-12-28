from  app.estudiorealizado.models import EstudioRealizado
from django.db.utils import IntegrityError
from utilidades.utilidades import Utilidades
from app.estudiorealizado.forms import EstudioRealizadoForm

# Create your views here.

class estudio_realizado_repository:

    def crear_estudio_realizado(self,request,*args, **kwargs):
        try:
            form = EstudioRealizadoForm(request.POST)
            if form.is_valid():
                form.save()
                return Utilidades.get_messages_200(self)
            else:
                return Utilidades.get_messages_400(self,'El datos no se pueden guardar por favor valide.')
            
        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
    

    def get_estudio_realizado(self,pk,*args, **kwargs):
        try:
            return EstudioRealizado.objects.filter(user_id=pk)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    
    def elimimanr_estudiio_realizado(self,pk):
        try:
            estudio_realizado=EstudioRealizado.objects.filter(pk=pk)
            estudio_realizado.delete()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
 
      
