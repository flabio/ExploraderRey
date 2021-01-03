from django.shortcuts import render,redirect 
from django.http import HttpResponse

from django.views.generic import TemplateView,View,ListView,UpdateView,CreateView,DeleteView
from django.contrib.auth.decorators import login_required
from  app.users.decorators import unauthenticated_user, allowed_users, admin_only
#locals
from django.urls import reverse,reverse_lazy

# Create your views here.


def destacamentoDashboard(request):
    return render(request, 'dashboard/index.html')
def ListaDashboard(request):
    return render(request, 'dashboard/index.html')
    


  
