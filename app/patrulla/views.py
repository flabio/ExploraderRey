from django.shortcuts import render
#plantilla
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
#exceptions
from django.core.exceptions import ObjectDoesNotExist
#http
from django.http import JsonResponse,HttpResponse
#core
from Infraestructure.Repository.patrulla.patrulla_repository import  patrulla_repository
from Negocios.Patrulla.patrulla_bl import  patrulla_bl
#utilidas
import json
#formulario
from .forms import PatrullaForm

class ListaPatrulla(View):
    form_class = PatrullaForm
    template_name = 'patrulla/index.html'
    
    try:
        def get_context_data(self,**kwargs):
            contexto = {}
            contexto['form'] = self.form_class()
            return contexto

        def get(self,request,*args,**kwargs):
            return render(request,self.template_name,self.get_context_data())
 
    except ObjectDoesNotExist as ex:
        error = ex

class ListaPatrullaJson(View):
    def get(self,request,*args,**kwargs):
        result = patrulla_bl.listado_patrulla(self)
        return HttpResponse(json.dumps({'data':result}, indent=4),content_type='application/json')
        
    
class CrearPatrulla(CreateView):
    """Crear Patrulla"""  
    def post(self,request,*args,**kwargs):
        result = patrulla_bl.crear_patrulla(self,request)
        return JsonResponse(result)

class EditarPatrulla(UpdateView):
    """Update Patrulla view."""
    def post(self,request,pk,*args,**kwargs):
        result = patrulla_bl.editar_patrulla(self,request,pk)
        return JsonResponse(result)
  
class EliminarPatrulla(View):
    def get(self, request,pk, *args, **kwargs):
        result=patrulla_bl.eliminar_patrulla(self,pk)
        return JsonResponse(result)
        
    
       
