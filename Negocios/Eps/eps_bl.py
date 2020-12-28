from Infraestructure.Repository.eps.eps_repository import  eps_reposity

from utilidades.utilidades import  Utilidades

class  eps_bl:
    def listado_eps(self,*args,**kwargs):
        return eps_reposity.listado_eps(self)
    
    def crear_eps(self,request,*args,**kwargs):
        if request.method=='POST':

            if len(request.POST.get('nombre'))==0:
                return Utilidades.get_messages_400(self,' The field name is required.')

            if eps_reposity.validar_nombre_existe(self,request.POST.get('nombre'))>0:
                return Utilidades.get_messages_400(self,'the name already exists.')

            else:
                return eps_reposity.crear_eps(self,request)
        else:
            return Utilidades.get_messages_400(self,'request error, must be post')

    def editar_eps(self,request,pk):

        if len(request.POST.get('nombre'))==0:
                return Utilidades.get_messages_400(self,' The field name is required.')
        if pk>0:
            return eps_reposity.editar_eps(self,request,pk)
        else:
            return Utilidades.get_messages_mayor_cero_400(self)
    
    def eliminar_eps(self,pk):
        if pk>0:
            return eps_reposity.eliminar_eps(self,pk)
        else:
            return Utilidades.get_messages_mayor_cero_400(self)
