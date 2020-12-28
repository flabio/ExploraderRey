# """Nivel Ministerial URLs."""

# Django
from django.urls import path
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from  app.users.decorators import unauthenticated_user, allowed_users, admin_only 
# View
from app.nivelministerial.views import ListaNivelMinisterial,ListaNivelMinisterialJson,CrearNivelMinisterial,EliminarNivelMinisterial


urlpatterns = [
    path(
        route='',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaNivelMinisterial.as_view())),
        name = 'index'
    ),

    path(
        route='lista-nivelministerial/<int:id>',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaNivelMinisterialJson.as_view())),
       
        name='lista-nivelministerial'
    ),
    path(
        route='crear-nivel-academico-ministeial',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (CrearNivelMinisterial.as_view())),
        name='crear-nivel-academico-ministeial'
    ),
    # path(
    #     route='editar/<int:pk>',
    #     view = login_required(
    #             allowed_users(allowed_roles=['admin','navegantes']) 
    #             (EditarIglesia.as_view())),
      
    #     name='editar'
    # ),
    path(
        route='eliminar/<int:pk>',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (EliminarNivelMinisterial.as_view())),
      
        name='eliminar'
    )
   

 ]