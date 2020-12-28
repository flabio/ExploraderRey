from Infraestructure.Repository.user_repository import userRepository
from utilidades.utilidades import  Utilidades
class admin_bl:
    def listaod_admin(self):
        return userRepository.listado_users(self,'admin')
    
    def crear_admin(self,request,*args,**kwargs):
        if request.method == 'POST':
            return userRepository.crear_users(self,request,'admin',1)
    
    def eliminar_admin(self,pk):
        if pk>0:
            return userRepository.Eliminar(self,pk)
        else:
            Utilidades.get_messages_mayor_cero_400(self)

        
        

