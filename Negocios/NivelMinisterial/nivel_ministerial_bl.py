from Infraestructure.Repository.nivelministerial.nivel_ministerial_repository import nivel_ministerial_repository
from django.db.utils import IntegrityError
from utilidades.utilidades import  Utilidades


class nivel_ministerial_bl:
    def listado_nivel_ministerial(self,pk,*args,**kwargs):
        return nivel_ministerial_repository.listado_nivel_ministerial(self,pk)
    def crear_nivel_ministerial(self,request,*args,**kwargs):
        try:
            if request.method=='POST':
    
                if len(request.POST.get('nombre'))==0:
                    return Utilidades.get_messages_400(self,' The field name is required.')
                
                if len(request.POST.get('lugar'))==0:
                    return Utilidades.get_messages_400(self,' The field lugar is required.')
                
                if len(request.POST.get('fecha'))==0:
                    return Utilidades.get_messages_400(self,' The field lugar is required.')
                
                else:
                    return nivel_ministerial_repository.crear_nivel_ministerial(self,request)
            else:
                return Utilidades.get_messages_400(self,'request error, must be post')

        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))

    def eliminar_nivel_ministerial(self,pk):
        
        if pk>0:
            return nivel_ministerial_repository.eliminar_nivel_ministerial(self,pk)
        else:
            Utilidades.get_messages_mayor_cero_400(self)

    def get_nivel_ministerial(self,pk):
        
        if pk>0:
            return nivel_ministerial_repository.get_nivel_ministerial(self,pk)
        else:
            Utilidades.get_messages_mayor_cero_400(self)
    

