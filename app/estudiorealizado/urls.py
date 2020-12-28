"""estudiorealizado URLs."""
# Django
from django.urls import path
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from  app.users.decorators import unauthenticated_user, allowed_users, admin_only 
# View
from app.estudiorealizado.views import CrearEstudioRealizado,EliminarEstudioRealizado


urlpatterns = [
    path(
        route='crear-estudio-realizado',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (CrearEstudioRealizado.as_view())),
        name='crear-estudio-realizado'
    ),
  
    path(
        route='eliminar/<int:pk>',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (EliminarEstudioRealizado.as_view())),
      
        name='eliminar'
    )

]