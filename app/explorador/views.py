
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, View,CreateView

from django.http import JsonResponse, HttpResponse

# forms
from Negocios.Users.users_bl import users_bl
from Negocios.Iglesia.iglesia_bl import iglesia_bl
# forms

from app.users.forms import CreateUserForm, PerfilFrom,EstudioRealizadoForm

# Create your views here.
class lista_explorador(View):

    template_name = 'explorador/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class crear_explorador(CreateView):
    
    form_class = CreateUserForm
    form_calss_perfil = PerfilFrom
    template_name = 'users/create.html'
    
    def get_context_data(self, rol,**kwargs):
        
        contexto = {}
        contexto['rol']=rol
        contexto['iglesia'] = iglesia_bl.listado_iglesia(self)
        contexto['form'] = self.form_class()
        contexto['form_perfil'] = self.form_calss_perfil()
        return contexto

    def get(self, request,rol, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(rol))

