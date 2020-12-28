"""iglesia URLs."""

# Django
from django.urls import path
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from  app.users.decorators import unauthenticated_user, allowed_users, admin_only 
# View
from app.iglesia.views import ListaIglesia,ListaIglesiaJson,CrearIglesia,EditarIglesia,EliminarIglesia,IglesiaApi


urlpatterns = [


    
    path(
        route='',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaIglesia.as_view())),
       
        name='index'
    ),
    path(
        route='lista-iglesia',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaIglesiaJson.as_view())),
       
        name='lista-iglesia'
    ),

    path(
        route='api-iglesia',
        view = IglesiaApi.as_view(),
        name='api-iglesia'
    ),
    path(
        route='crear-iglesia',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (CrearIglesia.as_view())),
        name='crear-iglesia'
    ),
    path(
        route='editar/<int:pk>',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (EditarIglesia.as_view())),
      
        name='editar'
    ),
    path(
        route='eliminar/<int:pk>',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (EliminarIglesia.as_view())),
      
        name='eliminar'
    )
    # path(
    #     route='users/signup/',
    #     view=views.signup,
    #     name='signup'
    # ),
    # path(
    #     route='users/me/profile/',
    #     view=views.update_profile,
    #     name='update_profile'
    # )

]