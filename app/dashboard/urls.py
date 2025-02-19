"""Users URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from  app.users.decorators import unauthenticated_user, allowed_users, admin_only
# View
from app.dashboard.views import ListaDashboard,destacamentoDashboard


urlpatterns = [

  
    path(
        route='index',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaDashboard)),
      
        name='index'
    ),
    path(
        route='dashboard-destacamento',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (destacamentoDashboard)),
      
        name='dashboard-destacamento'
    ),
 


]