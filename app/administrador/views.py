from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView,DetailView
from datetime import datetime, date, time, timedelta
# Exception
from django.db.utils import IntegrityError

#
from .utils import render_to_pdf
#
# Models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# locales


from Infraestructure.Repository.user_repository import  userRepository
from Infraestructure.Repository.groups.groupsRepository import groupsRepository

from Negocios.Administrador.admin_bl import  admin_bl
from Negocios.NivelMinisterial.nivel_ministerial_bl import nivel_ministerial_bl
from Negocios.EstudioRealizado.estudio_realizado_bl import estudio_realizado_bl
# forms
from app.users.forms import CreateUserForm, PerfilFrom,EstudioRealizadoForm
from app.nivelministerial.forms import NivelMinisterialForm
from app.users.models import Perfil
from app.iglesia.models import Iglesia
from app.nivelministerial.models import NivelMinisterial
from app.estudiorealizado.models import EstudioRealizado
from utilidades.utilidades import Utilidades
import json
import pdfkit
# Create your views here.


class ListaAdministrador(View):

    model = Perfil
    template_name = 'administrador/index.html'
    try:
        def get(self, request, *args, **kwargs):
            return render(request, self.template_name)
    except ObjectDoesNotExist as ex:
        error = ex


class RegistrarAdministrador(CreateView):

    model = User
    model_iglesia = Iglesia
    model_perfil = Perfil
    form_class = CreateUserForm
    form_calss_perfil = PerfilFrom
    template_name = 'administrador/create.html'

    def get_queryset_iglesia(self):
        return self.model_iglesia.objects.filter(estado=True).order_by('nombre')

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['iglesia'] = self.get_queryset_iglesia()
        contexto['form'] = self.form_class()
        contexto['form_perfil'] = self.form_calss_perfil()
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        result = admin_bl.crear_admin(self,request)
        return JsonResponse(result)
        

class ListaAdministradorJson(View):
    
    def get(self, request, *args, **kwargs):
        result = admin_bl.listaod_admin(self)
        return HttpResponse(json.dumps({'data': result}, indent=4),content_type='application/json')

    
class DetalleAdminstrador(DetailView):
    model = Perfil
    form_estudio_realizado = EstudioRealizadoForm
    form_nivel_aca_minis   = NivelMinisterialForm
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        nivel_ministerial = nivel_ministerial_bl.get_nivel_ministerial(self,self.object.user_id)
        estudio_realizado = estudio_realizado_bl.get_estudio_realizado(self,self.object.user_id)
        
        context = self.get_context_data(object=self.object,nivel_ministerial = nivel_ministerial,estudio_realizado=estudio_realizado,form_estudio_realizado=self.form_estudio_realizado(),form_nivel_aca_minis=self.form_nivel_aca_minis())
        return self.render_to_response(context)

class PerfilPdfView(View):
    model = Perfil
    model_nivel = NivelMinisterial
    model_estudio_realizado = EstudioRealizado

    try:
        def get(self, request, pk, *args, **kwargs):
            object  = Perfil.objects.get(pk = pk)
            nivel_ministerial = self.model_nivel.objects.filter(user_id=object.user_id)
            estudio_realizado = self.model_estudio_realizado.objects.filter(user_id=object.user_id)
        
            return render(request,'administrador/hoja_vida.html',{'perfil':object,'nivel_ministerial':nivel_ministerial,'estudio_realizado':estudio_realizado})
    except ObjectDoesNotExist as ex:
        error_alerta = ex
        
class pdfDetalle(View):
    model = Perfil
    try:
        def get(self, request, pk,*args, **kwargs):
            
            options = {
                'page-size': 'A4',
                'margin-top': '0.1in',
                'margin-right': '0.1in',
                'margin-bottom': '0.1in',
                'margin-left': '0.1in',
                'encoding': "UTF-8",
            }
            config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
           
            if config:
                pdf = pdfkit.from_url('http://127.0.0.1:8000/administrador/detalle-pdf/'+str(pk), False,configuration=config, options=options)

                if pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    filename = ("FT-003_HOJA_DE_VIDA_DE_LIDERES.pdf")
                    content = "inline; filename=%s" %(filename)
                    response['Content-Disposition'] = content
                    download = request.GET.get("download")

                    if download:
                        content = "attachment; filename=%s" %(filename)

                    response['Content-Disposition'] = content
                    return response
            return HttpResponse("Not found")
    except ObjectDoesNotExist as ex:
        error_alerta = ex
  
class EditarAdminitrador(View):
    """Update Administrador view."""
    model = User
  
    model_perfil = Perfil
    form_class = CreateUserForm
    form_calss_perfil = PerfilFrom
    template_name = 'administrador/editar.html'

   
    def get_queryset_perfil(self,pk):
        return self.model_perfil.objects.get(user_id=pk)
    def get_context_data(self,pk, **kwargs):
        contexto = {}
      
        contexto['form'] = self.form_class()
        contexto['form_perfil'] = self.form_calss_perfil()
        contexto['perfil'] = self.get_queryset_perfil(pk)
        contexto['pk'] = pk
        return contexto

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.get_context_data())

    def get(self, request,pk, *args, **kwargs):

        """Handle GET requests: instantiate a blank version of the form."""
        
        return render(request, self.template_name, self.get_context_data(pk))
    def post(self, request, *args, **kwargs):
        result =admin_bl.crear_admin(self,request)
        return JsonResponse(result)
           
class EliminarUsers(DeleteView):

    def get(self, request, pk, *args, **kwargs):

        try:
            result = admin_bl.eliminar_admin(self,pk)
            return JsonResponse(result)
        except IntegrityError as error:
            data = {
                'status':  500,
                'existe':  True,
                'estado':  'warning',
                'message':  ' '+str(error.args[1])
            }
            return JsonResponse(data)
