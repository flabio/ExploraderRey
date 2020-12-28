from Infraestructure.Repository.destacamento.destacamento_repository import  destacamento_repository
from utilidades.utilidades import  Utilidades
import  utilidades.validar as v
class destacamento_bl:
    def listado_destacamento(self):
        return destacamento_repository.listado_destacamento(self)
    
    def create_destacamento(self,request,*args,**kwargs):
        if request.method=='POST':
            if v.validar_campo_vacio(request.POST.get('nombre')):
                return Utilidades.get_messages_400(self,' The field name is required.')

            if v.validar_campo_vacio(request.POST.get('distrito')):
                return Utilidades.get_messages_400(self,' The field distrito is required.')
            
            if v.validar_campo_vacio(request.POST.get('numero')):
                return Utilidades.get_messages_400(self,' The field number is required.')
            
            if v.validar_campo_vacio(request.POST.get('seccion')):
                return Utilidades.get_messages_400(self,' The field seccion is required.')

            if v.validar_campo_vacio(request.POST.get('iglesia')):
                return Utilidades.get_messages_400(self,' The field iglesia is required.')
            else:
                return destacamento_repository.create_destacamento(self,request)
        else:
            return Utilidades.get_messages_400(self,'request error, must be post')

    def get_editar_destacamento(self,request,pk,*args,**kwargs):
        if request.method=='POST':
            
            if len(request.POST.get('nombre'))==0:
                return Utilidades.get_messages_400(self,' The field name is required.')

            if len(request.POST.get('distrito'))==0:
                return Utilidades.get_messages_400(self,' The field distrito is required.')
            
            if len(request.POST.get('numero'))==0:
                return Utilidades.get_messages_400(self,' The field number is required.')
            
            if len(request.POST.get('seccion'))==0:
                return Utilidades.get_messages_400(self,' The field seccion is required.')

            if len(request.POST.get('iglesia'))==0:
                return Utilidades.get_messages_400(self,' The field iglesia is required.')
            
            if pk==0:
                return Utilidades.get_messages_mayor_cero_400(self)
            else:
                return destacamento_repository.get_editar_destacamento(self,request,pk)
        else:
            return Utilidades.get_messages_400(self,'request error, must be post')
    
    def eliminar_destacamento(self,pk):
        if pk>0:
            return destacamento_repository.eliminar_destacamento(self,pk)
        else:
            return Utilidades.get_messages_mayor_cero_400(self)
    
    def get_queryset_iglesia(self):
        return destacamento_repository.get_queryset_iglesia(self)
    
    def get_queryset_seccion(self):
        return destacamento_repository.get_queryset_seccion(self)
    
    def get_queryset_grupo(self):
        return destacamento_repository.get_queryset_grupo(self)

    def get_queryset_destcamento(self,pk):
        return destacamento_repository.get_queryset_destcamento(self,pk)

    def get_create_grupo_destacamento(self,request):
        return destacamento_repository.get_create_grupo_destacamento(self,request)
    
    def listado_grupo_destacamento(self,pk):
        return destacamento_repository.listado_grupo_destacamento(self,pk)
    
    def eliminar_grupo_destacamento(self,pk):
        return destacamento_repository.eliminar_grupo_destacamento(self,pk)
