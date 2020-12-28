from Infraestructure.Repository.estudiorealizado.estudio_realizado_repository import estudio_realizado_repository
from utilidades.utilidades import  Utilidades
from django.db.utils import IntegrityError 
class estudio_realizado_bl:
    def crear_estudio_realizado(self,request,*args,**kwargs):
        try:
            if request.method=='POST':
    
                if len(request.POST.get('num_semestre'))==0:
                    return Utilidades.get_messages_400(self,' The field name is required.')
                else:
                    return estudio_realizado_repository.crear_estudio_realizado(self,request)
            else:
                return Utilidades.get_messages_400(self,'request error, must be post')

        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))

    def get_estudio_realizado(self,pk):
        
        if pk>0:
            return estudio_realizado_repository.get_estudio_realizado(self,pk)
        else:
            Utilidades.get_messages_mayor_cero_400(self)

    def elimimanr_estudiio_realizado(self,pk):
        
        if pk>0:
            return estudio_realizado_repository.elimimanr_estudiio_realizado(self,pk)
        else:
            Utilidades.get_messages_mayor_cero_400(self)
    

