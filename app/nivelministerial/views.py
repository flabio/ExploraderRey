from django.shortcuts import render,redirect 
from django.http import HttpResponse,JsonResponse
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse,reverse_lazy

from Negocios.NivelMinisterial.nivel_ministerial_bl import nivel_ministerial_bl
from .forms import NivelMinisterialForm
import json
# Create your views here.

class ListaNivelMinisterial(View):
    form_class = NivelMinisterialForm
    template_name = 'nivelministerial/index.html'
    
    try:

        def get_context_data(self,**kwargs):
            contexto = {}
            contexto['form'] = self.form_class()
            return contexto

        def get(self,request,*args,**kwargs):
            return render(request,self.template_name,self.get_context_data())
 
    except ObjectDoesNotExist as ex:
        error = ex
class ListaNivelMinisterialJson(View):
   
    def get_queryset(self,id):
        return  self.model.objects.filter(user_id=id).order_by('created')
    
    def get(self,request,id,*args,**kwargs):
        result = nivel_ministerial_bl.listado_nivel_ministerial(self,id)
        return HttpResponse(json.dumps({'data':result},indent=1),content_type='application/json')
    
class CrearNivelMinisterial(CreateView):  
    def post(self,request,*args,**kwargs):
        result = nivel_ministerial_bl.crear_nivel_ministerial(self,request)
        return JsonResponse(result)
            
class EliminarNivelMinisterial(View):

    def get(self, request,pk, *args, **kwargs):
        result = nivel_ministerial_bl.eliminar_nivel_ministerial(self,pk)
        return JsonResponse(result)
            
