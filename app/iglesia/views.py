from django.shortcuts import render 
from django.http import JsonResponse,HttpResponse
from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
# web api
from rest_framework.views import APIView
from  rest_framework import  serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

#utilidas
import json
#locals

from Negocios.Iglesia.iglesia_bl import  iglesia_bl
from .models import Iglesia
from .forms import IglesiaForm
from .serializers import IglesiaSerializer
# Create your views here.

class ListaIglesia(View):
    model = Iglesia
    form_class = IglesiaForm
    template_name = 'iglesia/index.html'
   
    def get(self,request,*args,**kwargs):
        context={}
        context['form']=self.form_class()
        return render(request,self.template_name,context)

class ListaIglesiaJson(View):

    def get(self,request,*args,**kwargs):
        result = iglesia_bl.listado_iglesia(self)
        return HttpResponse(json.dumps({'data':result},indent=4),content_type='application/json')

class CrearIglesia(CreateView):  
    form_class = IglesiaForm
    def post(self,request,*args,**kwargs):
        if request.method=='POST':
            result = iglesia_bl.create_iglesia(self,request)
            return JsonResponse(result)
        
class EditarIglesia(UpdateView):
    model = Iglesia
    form_class = IglesiaForm
    template_name = 'iglesia/crear_iglesia.html'
    def post(self,request,pk,*args,**kwargs):
        result = iglesia_bl.get_editar_iglesia(self,request,pk)
        return JsonResponse(result)

class EliminarIglesia(View):
    def get(self, request,pk, *args, **kwargs):
        result = iglesia_bl.eliminar_iglesia(self,pk)
        return JsonResponse(result)
        
        
""" web api """
class IglesiaApi(APIView):
    
    def get(self,request,format=None):
        result = iglesia_bl.listado_iglsia(self)
        serializer = IglesiaSerializer(result, many=True)
        return Response(serializer.data)
        
    def post(self,request):
        result = iglesia_bl.create_iglesia(self,request.data,0)
        return Response(result)

    def put(self,request):
        print(request)
        
    def delete(self,request):
        result = iglesia_bl.eliminar_iglesia(request.data)
        return Response(result)