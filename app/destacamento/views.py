from django.shortcuts import render
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
from django.http import JsonResponse,HttpResponse
#
from Infraestructure.Repository.destacamento.destacamento_repository import destacamento_repository
from Negocios.Destacamento.destacamento_bl import  destacamento_bl
#utilidades
import json
#locales
from .forms import DestacamentoForm
# Create your views here.
class ListaDestacamento(View):
   
    form_Class      = DestacamentoForm
    template_name   = 'destacamento/index.html'
   
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['form']    = self.form_Class()
        contexto['iglesia'] = destacamento_bl.get_queryset_iglesia(self)
        contexto['seccion'] = destacamento_bl.get_queryset_seccion(self)
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
    
class ListaDestacamentoJson(View):
    def get(self,request,*args,**kwargs):
        result = destacamento_bl.listado_destacamento(self)
        return HttpResponse(json.dumps({'data':result}, indent=4),content_type='application/json')

class CrearDestacamento(CreateView):
    
    def post(self,request,*args,**kwargs):
        result = destacamento_bl.create_destacamento(self,request)
        return JsonResponse(result)

class EditarDestacamento(UpdateView):
    """Update Destacamento view."""
    
    def post(self,request,pk,*args,**kwargs):
        result = destacamento_bl.get_editar_destacamento(self,request,pk)
        return JsonResponse(result)

class EliminarDestacamento(View):
    def get(self, request,pk, *args, **kwargs):
        result = destacamento_bl.eliminar_destacamento(self,pk)
        return JsonResponse(result)

"""grupo detacamento"""
class DestacamentoDetalleView(TemplateView):
    template_name='destacamento/detalle.html'
  
    def get_context_data(self,pk, **kwargs):
        """Add user's posts to context."""
        context                  = super().get_context_data(**kwargs)
        context['grupos']        = destacamento_bl.get_queryset_grupo(self)
        context['destacamento']  = destacamento_bl.get_queryset_destcamento(self,pk)
        
        return context

class CrearGrupoDestacamento(CreateView):
   
    def post(self,request,*args,**kwargs):
        result = destacamento_bl.get_create_grupo_destacamento(self,request)
        return JsonResponse(result)

class ListaGrupoDestacamentoJson(View):
        
    def get(self,request,pk,*args,**kwargs):
        result = destacamento_bl.listado_grupo_destacamento(self,pk)
        return HttpResponse(json.dumps({'data':result}, indent=4),content_type='application/json')

class EliminarGrupoDestacamento(View):
  
    def get(self, request,pk, *args, **kwargs):
        result = destacamento_bl.eliminar_grupo_destacamento(self,pk)
        return JsonResponse(result)