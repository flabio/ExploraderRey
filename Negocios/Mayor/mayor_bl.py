from Infraestructure.Repository.user_repository import userRepository
from utilidades.utilidades import  Utilidades

class mayor_bl:
    
    def get_perfil(self,pk):
        return userRepository.get_perfil(self,pk)
    
    def listaod_mayores(self):
        return userRepository.listado_users(self,'mayor')
    
    def crear_mayor(self,request,*args,**kwargs):
        return userRepository.crear_users(self,request,'mayor',1)
    
    def eliminar_usuario(self,pk,*args,**kwargs):
        if pk>0:
            return userRepository.Eliminar(self,pk)
        else:
            Utilidades.get_messages_mayor_cero_400(self)

