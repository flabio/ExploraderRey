from django.shortcuts import render,redirect 
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.http import JsonResponse
from Negocios.EstudioRealizado.estudio_realizado_bl import estudio_realizado_bl
# Create your views here.
class CrearEstudioRealizado(CreateView):  
    
    def post(self,request,*args,**kwargs):
        result = estudio_realizado_bl.crear_estudio_realizado(self,request)
        return JsonResponse(result)
            
class EliminarEstudioRealizado(View):
    
    def get(self, request,pk, *args, **kwargs):
        result = estudio_realizado_bl.elimimanr_estudiio_realizado(self,pk)
        return JsonResponse(result)
        
    
