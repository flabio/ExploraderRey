from Infraestructure.Repository.user_repository import userRepository
from utilidades.utilidades import  Utilidades

class users_bl:
    def get_perfil(self,pk):
        return userRepository.get_perfil(self,pk)

    def listaod_users(self,rol):
        return userRepository.listado_users(self,rol)
    
    def crear_user(self,request,rol,superuser,*args,**kwargs):
        return userRepository.crear_users(self,request,rol,superuser)

    def eliminar_user(self,pk):
        return userRepository.Eliminar(self,pk)
    