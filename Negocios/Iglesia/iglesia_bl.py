from Infraestructure.Repository.Iglesia.iglesia_repository import  iglesia_repository
from utilidades.utilidades import  Utilidades

class iglesia_bl:
    def listado_iglesia(self):
        return iglesia_repository.listado_iglsia(self)
    
    def create_iglesia(self,request,*args,**kwargs):
        if len(request.POST.get('nombre'))==0:
            return Utilidades.get_messages_400(self,'El campo nombre es requerido.')

        if len(request.POST.get('direccion'))==0:
            return Utilidades.get_messages_400(self,'El campo dirección es requerido.')
        
        if len(request.POST.get('telefono'))==0:
            return Utilidades.get_messages_400(self,'El campo teléfono es requerido.')
        
        if len(request.POST.get('correo'))==0:
            return Utilidades.get_messages_400(self,'El campo correo es requerido.')
        
        else:
            return iglesia_repository.create_iglesia(self,request)

    def get_editar_iglesia(self,request,pk,*args,**kwargs):
        if pk==0:
            return Utilidades.get_messages_mayor_cero_400(self)
        if len(request.POST.get('nombre'))==0:
            return Utilidades.get_messages_400(self,'El campo nombre es requerido.')

        if len(request.POST.get('direccion'))==0:
            return Utilidades.get_messages_400(self,'El campo dirección es requerido.')
        
        if len(request.POST.get('telefono'))==0:
            return Utilidades.get_messages_400(self,'El campo teléfono es requerido.')
        
        if len(request.POST.get('correo'))==0:
            return Utilidades.get_messages_400(self,'El campo correo es requerido.')
        
        else:
            return iglesia_repository.get_editar_iglesia(self,request,pk)
          
    def eliminar_iglesia(self,pk):
        if pk==0:
            return Utilidades.get_messages_mayor_cero_400(self)
        else:
            return iglesia_repository.eliminar_iglesia(self,pk)
