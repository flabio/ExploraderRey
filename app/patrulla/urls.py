"""destacamento urls"""

# django
from django.urls import path
from django.contrib.auth.decorators import login_required
#locals
from app.users.decorators import unauthenticated_user,allowed_users,admin_only

# Views
from app.patrulla.views import ListaPatrulla,ListaPatrullaJson,CrearPatrulla,EditarPatrulla,EliminarPatrulla

urlpatterns =[
    path(
        route='',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (ListaPatrulla.as_view())
        ),
        name='index'
    ),
    path(
        route='lista-patrulla',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaPatrullaJson.as_view())),
        name='lista-patrulla'
    ),
    path(
        route='crear-patrulla',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (CrearPatrulla.as_view())
        ),
        name='crear-patrulla'
    ),
    path(
        route='editar-patrulla/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EditarPatrulla.as_view())
        ),
        name='editar-patrulla'
    ),
    path(
        route='eliminar-patrulla/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EliminarPatrulla.as_view())
        ),
        name='eliminar-patrulla'
    ),
    
]
