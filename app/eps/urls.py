"""grupo urls"""

# django
from django.urls import path
from django.contrib.auth.decorators import login_required
#locals
from app.users.decorators import unauthenticated_user,allowed_users,admin_only

# Views
from app.eps.views import ListaEps,ListaEpsJson,CrearEps,EliminarEps,EditarEps

urlpatterns =[
    path(
        route='',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (ListaEps.as_view())
        ),
        name='index'
    ),
    path(
        route='lista-eps',
        view = login_required(
                allowed_users(allowed_roles=['admin']) 
                (ListaEpsJson.as_view())),
        name='lista-eps'
    ),
    path(
        route='crear-eps',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (CrearEps.as_view())
        ),
        name='crear-eps'
    ),
     path(
        route='editar-eps/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EditarEps.as_view())
        ),
        name='editar-eps'
    ),
      path(
        route='eliminar-eps/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EliminarEps.as_view())
        ),
        name='eliminar-eps'
    )
]
