"""Admins URLs."""
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from app.users.decorators import unauthenticated_user, allowed_users, admin_only

# View
from app.administrador.views import ListaAdministrador, RegistrarAdministrador, EliminarUsers, ListaAdministradorJson,EditarAdminitrador,DetalleAdminstrador,pdfDetalle,PerfilPdfView

urlpatterns = [

    path(
        route='listado-admin/',
        view=login_required(
            allowed_users(allowed_roles=['admin'])
            (ListaAdministrador.as_view())),
        name='listado-admin'
    ),
    path(
        route='lista-adminjson/',
        view=login_required(
            allowed_users(allowed_roles=['admin'])
            (ListaAdministradorJson.as_view())),
        name='lista-adminjson'
    ),
    
    path(
        route='registrar-admin/',
        view=login_required(
            allowed_users(allowed_roles=['admin'])
            (RegistrarAdministrador.as_view())),
        name='registrar-admin'
    ),
    path(
        route = 'detalle/<int:pk>',
        view  = login_required(allowed_users(allowed_roles=['admin'])
                (DetalleAdminstrador.as_view())),
        name  = 'detalle' 
    ),
     path(
        route = 'pdf-detalle/<int:pk>',
        view  =pdfDetalle.as_view(),
        name  = 'pdf-detalle' 
    ),
path(
    route ='detalle-pdf/<int:pk>',
    view  = PerfilPdfView.as_view(),
    name ='detalle-pdf'
),
    path(
        route='editar/<int:pk>',
        view=login_required(
            allowed_users(allowed_roles=['admin'])
            (EditarAdminitrador.as_view())),
        name='editar'

    ),
    path(
        route='eliminar/<int:pk>',
        view=login_required(
            allowed_users(allowed_roles=['admin'])
            (EliminarUsers.as_view())),
        name='eliminar'
    )

]
