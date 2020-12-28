from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpResponse

# negocios
from Negocios.Grupo.grupo_bl import  grupo_bl
#utilidas
import json

#locals
from .forms import GrupoForm

class ListaGrupo(View):
    
    form_class = GrupoForm
    template_name = 'grupo/index.html'
    
    try:
        
        def get_context_data(self,**kwargs):
            contexto = {}
            contexto['form'] = self.form_class()
            return contexto

        def get(self,request,*args,**kwargs):
            return render(request,self.template_name,self.get_context_data())
 
    except ObjectDoesNotExist as ex:
        error = ex
class ListaGrupoJson(View):
    def get(self,request,*args,**kwargs):
        datos=[]
        result = grupo_bl.listado_grupo(self)
        return HttpResponse(json.dumps({'data':result}, indent=4),content_type='application/json')
    
class CrearGrupo(CreateView):
    """Crear Grupo"""  
    def post(self,request,*args,**kwargs):
        result = grupo_bl.crear_grupo(self,request)
        return JsonResponse(result)
            
class EditarGrupo(UpdateView):
    """Update Grupo view."""
    def post(self,request,pk,*args,**kwargs):
        result = grupo_bl.editar_grupo(self,request,pk)
        return JsonResponse(result)
  
class EliminarGrupo(View):
   
    def get(self, request,pk, *args, **kwargs):
        result = grupo_bl.eliminar_grupo(self,pk)
        return JsonResponse(result)
        
    
