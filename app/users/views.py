from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse

from django.views.generic import TemplateView, View, ListView, UpdateView, CreateView, DeleteView
from datetime import datetime, date, time, timedelta
# Exception




# locales
from Negocios.Users.users_bl import users_bl
from Negocios.Iglesia.iglesia_bl import iglesia_bl
# forms

from .forms import CreateUserForm, PerfilFrom

import json
# Create your views here.

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'
    
class lista_users_json(View):
    def get(self, request,valor, *args, **kwargs):
        result = users_bl.listaod_users(self,valor)
        return HttpResponse(json.dumps({'data': result}, indent=4),content_type='application/json')
class crear_user(CreateView):
    def post(self, request, *args, **kwargs):
        
        result = users_bl.crear_user(self,request,request.POST.get('group'),1)
        return HttpResponse(json.dumps({'data': result}, indent=4),content_type='application/json')

class editar_user(UpdateView):
    
    form_class = CreateUserForm
    form_calss_perfil = PerfilFrom
    template_name = 'users/editar.html'

    def get_context_data(self,pk, rol,**kwargs):
        contexto = {}
        contexto['iglesia'] = iglesia_bl.listado_iglesia(self)
        contexto['form'] = self.form_class()
        contexto['form_perfil'] = self.form_calss_perfil()
        contexto['perfil'] = users_bl.get_perfil(self,pk)
        contexto['pk'] = pk
        contexto['rol'] = rol
        return contexto
    def get(self, request,pk,rol, *args, **kwargs):

        """Handle GET requests: instantiate a blank version of the form."""
        return render(request, self.template_name, self.get_context_data(pk,rol))
    def post(self, request, *args, **kwargs):
        result = users_bl.crear_user(self,request,request.POST.get('group'),1)
        print(result)
        return JsonResponse(result)

class EliminarUsers(DeleteView):
    
    def get(self, request, pk, *args, **kwargs):
        result = users_bl.eliminar_user(self,pk)
        return JsonResponse(result)

# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('users:login')

# @login_required
# def RegistrarUsers(request):
#     form = CreateUserForm()

#     if request.method=='POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             group = Group.objects.get(name='customer')
#             user.groups.add(group)
#     context = {'form':form}
#     return render(request,'users/registrar.html',context)


# @login_required
# def signup(request):
#     """Sign up view."""
#     if request.method == 'POST':
#         username = request.POST['username']
#         passwd = request.POST['passwd']
#         passwd_confirmation = request.POST['passwd_confirmation']

#         if passwd != passwd_confirmation:
#             return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

#         try:
#             user = User.objects.create_user(username=username, password=passwd)
#         except IntegrityError:
#             return render(request, 'users/signup.html', {'error': 'Username is already in user'})

#         user.first_name = request.POST['first_name']
#         user.last_name = request.POST['last_name']
#         user.email = request.POST['email']
#         user.save()

#         # profile = Profile(user=user)
#         # profile.save()

#         return redirect('login')

#     return render(request, 'users/signup.html')
