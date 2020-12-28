from Infraestructure.Repository.patrulla.patrulla_repository import  patrulla_repository
from utilidades.utilidades import Utilidades

class patrulla_bl:
    def listado_patrulla(self):
        return patrulla_repository.listado_patrulla(self)
    
    def crear_patrulla(self,request,*args,**kwargs):
        if request.method=='POST':
            
            if len(request.POST.get('nombre'))==0:
                return Utilidades.get_messages_400(self,' The field name is required.')

            if len(request.POST.get('grupo'))==0:
                return Utilidades.get_messages_400(self,' The field grupo is required.')
            else:
                return patrulla_repository.crear_patrulla(self,request)
        else:
            return Utilidades.get_messages_400(self,'request error, must be post')
    
    def editar_patrulla(self,request,pk):
        
        if len(request.POST.get('nombre'))==0:
                return Utilidades.get_messages_400(self,' The field name is required.')
        
        if len(request.POST.get('grupo'))==0:
            return Utilidades.get_messages_400(self,' The field grupo is required.')
        
        if pk>0:
            return patrulla_repository.editar_patrulla(self,request,pk)
        else:
            return Utilidades.get_messages_mayor_cero_400(self)
    
    def eliminar_patrulla(self,pk):
        if pk>0:
            return patrulla_repository.eliminar_patrulla(self,pk)
        else:
            return Utilidades.get_messages_mayor_cero_400(self)