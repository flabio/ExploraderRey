
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView,DetailView

# Models
from django.contrib.auth.models import User
from app.users.models import Perfil
from app.iglesia.models import Iglesia



from Negocios.Users.users_bl import users_bl
from Negocios.Iglesia.iglesia_bl import iglesia_bl
# forms

from app.users.forms import CreateUserForm, PerfilFrom,EstudioRealizadoForm
import json

# Create your views here.
class lista_capellan(View):

    template_name = 'capellan/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class crear_capellan(CreateView):
    
    form_class = CreateUserForm
    form_calss_perfil = PerfilFrom
    template_name = 'users/create.html'
    
    def get_context_data(self,rol, **kwargs):
        contexto = {}
        contexto['iglesia'] = iglesia_bl.listado_iglesia(self)
        contexto['form'] = self.form_class()
        contexto['form_perfil'] = self.form_calss_perfil()
        contexto['rol']=rol
        return contexto

    def get(self, request,rol, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(rol))


