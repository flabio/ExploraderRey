from app.destacamento.models import Destacamento
from app.iglesia.models import  Iglesia
from app.seccion.models import  Seccion
from app.grupodestacamento.models import GrupoDestacamento
from app.grupos.models import Grupos

from django.db.utils import IntegrityError
from utilidades.utilidades import Utilidades
import  utilidades.validar as v
# forms
from .forms import DestacamentoForm

# Create your views here.

class destacamento_repository:
    model = Destacamento
    model_util = Utilidades
     
    def listado_destacamento(self,*args, **kwargs):
        try:
            result = Destacamento.objects.filter()
            return [{'destacamento_id':item.pk,
                    'nombre':v.validar_campo_string(item.nombre),
                    'imagen':str(item.imagen),
                    'distrito':item.distrito,
                    'numero':item.numero,
                    'seccion':item.seccion.seccion,
                    'seccion_id':item.seccion.seccion_id,
                    'iglesia':v.validar_campo_string(item.iglesia.nombre),
                    'iglesia_id':item.iglesia.iglesia_id,
                    'comandante':v.validar_campo_string(item.seccion.user.first_name+" "+item.seccion.user.last_name),
                    'estado':item.estado,
                    'created':str(item.created)} for item in result]
        
        except IntegrityError as error:
            return Utilidades.get_messages_400(self,'No existe datos.'+str(error.args[1]))
    def create_destacamento(self,request,*args,**kwargs):
        
        try:
            
            if destacamento_repository.get_numero_existe(self,request.POST.get('numero'))>0:
                return Utilidades.gets_messages_400(self,'número','El número ya está asignado a  otro destacamento')
            
            form=DestacamentoForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return Utilidades.get_messages_200(self)
            else:
                return Utilidades.get_messages_400(self,'no se puede registrar la datos.'+str(request.POST))
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
   
    def get_editar_destacamento(self, request,pk, *args, **kwargs):
        try:
            
            destacamento = Destacamento.objects.get(destacamento_id=pk)
            if len(request.FILES)>0:
                destacamento.imagen = request.FILES['imagen']
           
            destacamento.nombre         =  request.POST.get('nombre')
            destacamento.distrito       =   request.POST.get('distrito')
            destacamento.numero         =   request.POST.get('numero')
            destacamento.seccion_id     =   request.POST.get('seccion')
            destacamento.iglesia_id     =   request.POST.get('iglesia')
            destacamento.estado         =   Utilidades.validar_estado(self,request.POST.get('estado'))
            destacamento.save()
            return Utilidades.get_messages_200(self)
            
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,'Error de servidor.'+str(error.args[1]))
  
    def eliminar_destacamento(self,pk,*args,**kwargs):
        try:
            if destacamento_repository.get_queryset_grupo_destcamento(self,pk)>0:
                return Utilidades.get_messages_400(self,'El Destacamenro no se puede eliminar esta asociado a un Grupo.')
            
            object = Destacamento.objects.get(pk=pk)
            object.delete()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    def get_numero_existe(self,numero):
         return Destacamento.objects.filter(numero=numero).count()
    
    def get_queryset_grupo_destcamento(self,pk):
        try:
            return GrupoDestacamento.objects.filter(destacamento_id=pk).count()
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))
    def get_queryset_iglesia(self):
            return Iglesia.objects.filter(estado=True).order_by('nombre')
    def get_queryset_seccion(self):
        return Seccion.objects.filter(estado = True).order_by('seccion')
    def get_queryset_grupo(self):
        return Grupos.objects.filter(estado=True)
    def get_queryset_destcamento(self,pk):
        return Destacamento.objects.get(pk=pk)
    def get_create_grupo_destacamento(self,request,*args,**kwargs):
            try:
                
                grupo_destacamento = GrupoDestacamento()
                grupo_destacamento.dgrupo_id        = request.POST.get('dgrupo')
                grupo_destacamento.destacamento_id  = request.POST.get('destacamento')
                
                if destacamento_repository.get_queryset_comprar_existe(self,request)>0:
                    return Utilidades.get_messages_400(self,'El destacamento ya tiene este grupo que selecciono asigando.')
                else:
                    grupo_destacamento.save()
                    return Utilidades.get_messages_200(self)
            except IntegrityError as error:
                return Utilidades.get_messages_400(self,'No existe datos.'+str(error.args[1]))
    def get_queryset_comprar_existe(self,request):
        return GrupoDestacamento.objects.filter(destacamento_id = request.POST.get('destacamento'),dgrupo_id = request.POST.get('dgrupo')).count()
    def listado_grupo_destacamento(self,pk,*args, **kwargs):
        try:
            datos = []
            if pk>0:
                result = GrupoDestacamento.objects.filter(destacamento_id=pk)
            else:
                result = GrupoDestacamento.objects.filter()
            for item in result:
                lista={
                   'pk':item.pk,
                    'nombre':item.dgrupo.nombre,
                    'grupo_id':item.dgrupo.grupo_id,
                    'destacamento_id':item.destacamento.destacamento_id,
                    'imagen':str(item.dgrupo.imagen),
                    'created':str(item.created)
                }
                datos.append(lista)
            return datos
        except IntegrityError as error:
            return self.model_util.get_messages_400(self,'No existe datos.'+str(error.args[1]))
    def eliminar_grupo_destacamento(self,pk,*args,**kwargs):
        try:
            object = GrupoDestacamento.objects.get(pk=pk)
            object.delete()
            return Utilidades.get_messages_200(self)
        except IntegrityError as error:
            return Utilidades.get_messages_500(self,str(error.args[1]))