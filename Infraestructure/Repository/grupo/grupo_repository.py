#models
from app.grupos.models import  Grupos
from app.grupodestacamento.models import  GrupoDestacamento
#formulario
from app.grupos.forms import  GrupoForm

from django.db.utils import  IntegrityError
#
from utilidades.utilidades import  Utilidades
import  utilidades.validar as v

class grupo_repository:
    def  listo_grupos(self):
        try:
            grupo = Grupos.objects.all().order_by('-created')
            return [{'grupo_id':item.pk,
                    'nombre':v.validar_campo_string(item.nombre),
                    'imagen':str(item.imagen),
                    'estado':item.estado,
                    'created':str(item.created),
                    'modified':str(item.modified)} for item in grupo]
       
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,'Error de services'+str(error.args[0]))

    def crear_grupo(self,request,*args,**kwargs):
        try:
            form=GrupoForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
    
    def editar_grupo(self,request,pk,*args,**kwargs):
        try:
            grupo=Grupos.objects.get(grupo_id=pk)
            if len(request.FILES)>0:
                grupo.imagen = request.FILES['imagen']
            grupo.nombre = request.POST.get('nombre')
            grupo.estado = Utilidades.validar_estado(request.POST.get('estado'))
            grupo.save()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
    
    def grupo_existe_nombre(self,nombre):
        try:
            return Grupos.objects.filter(nombre=nombre).count()
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))

    def eliminar_grupo(self,pk):
        try:
            result = Grupos.objects.get(grupo_id=pk)
            result.delete()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[0]))
    def consulta_id_grupo_destacamento(self,pk):
        return GrupoDestacamento.objects.filter(dgrupo_id=pk).count()