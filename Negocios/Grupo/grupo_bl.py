from Infraestructure.Repository.grupo.grupo_repository import  grupo_repository
from utilidades.utilidades import  Utilidades
from django.db.utils import  IntegrityError

class grupo_bl:
    def listado_grupo(self):
        return grupo_repository.listo_grupos(self)
    
    def crear_grupo(self,request,*args,**kwargs):
        try:
            if request.method=='POST':
    
                if len(request.POST.get('nombre'))==0:
                    return Utilidades.get_messages_400(self,' The field name is required.')
                if grupo_repository.grupo_existe_nombre(self,request.POST.get('nombre'))>0:
                    return Utilidades.get_messages_400(self,'the name already exists.')
                else:
                    return grupo_repository.crear_grupo(self,request)
            else:
                return Utilidades.get_messages_400(self,'request error, must be post')

        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))

    def editar_grupo(self,request,pk,*args,**kwargs):
        try:
            if request.method=='POST':
    
                if len(request.POST.get('nombre'))==0:
                    return Utilidades.get_messages_400(self,' The field name is required.')
                
                if pk>0:
                    return Utilidades.get_messages_mayor_cero_400(self)
                
                else:
                    return grupo_repository.editar_grupo(self,request,pk)
            else:
                return Utilidades.get_messages_400(self,'request error, must be post')

        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))

    def eliminar_grupo(self,pk,*args,**kwargs):
        try:
            
            if grupo_repository.consulta_id_grupo_destacamento(self,pk)>0:
                return Utilidades.get_messages_400(self,'no se puede eliminar tiene destacamento asignado.')

            if pk>0:
                return grupo_repository.eliminar_grupo(self,pk)
            else:
                return Utilidades.get_messages_mayor_cero_400(self)

        except  IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
        