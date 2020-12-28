from Infraestructure.Repository.user_repository import userRepository
from utilidades.utilidades import  Utilidades

class capellan_bl:
    
    def listaod_capellan(self,rol):
        return userRepository.listado_users(self,rol)
    
    def crear_capellan(self,request,rol,*args,**kwargs):
        return userRepository.crear_users(self,request,rol,1)
    


