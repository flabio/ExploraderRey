from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpResponse

# layer of business
from Negocios.Eps.eps_bl import  eps_bl
#utilidas
import json
#locals

# from .models import Eps
from app.users.models import Perfil
from .forms import EpsForm

class ListaEps(View):
   
    form_class = EpsForm
    template_name = 'eps/index.html'
    
    try:
        
        def get_context_data(self,**kwargs):
            contexto = {}
            contexto['form'] = self.form_class()
            return contexto

        def get(self,request,*args,**kwargs):
            return render(request,self.template_name,self.get_context_data())
 
    except ObjectDoesNotExist as ex:
        error = ex

class ListaEpsJson(View):
    """Listado de eps"""
    def get(self,request,*args,**kwargs):
        result = eps_bl.listado_eps(self)
        return HttpResponse(json.dumps({'data':result}, indent=4),content_type='application/json')
    
class CrearEps(CreateView):
    """Crear Eps"""  
    def post(self,request,*args,**kwargs):
        result=eps_bl.crear_eps(self,request)
        return JsonResponse(result)
    
class EditarEps(UpdateView):
    """Update Eps view."""
    def post(self, request,pk, *args, **kwargs):
        result=eps_bl.editar_eps(self,request,pk)
        return JsonResponse(result)

class EliminarEps(View):
    model_perfil = Perfil
   
    def get_queryset_perfil(self,pk):
        return self.model_perfil.objects.filter(users_id=pk).count()
    
    def get(self, request,pk, *args, **kwargs):
        result=eps_bl.eliminar_eps(self,pk)
        return JsonResponse(result)
        
    
