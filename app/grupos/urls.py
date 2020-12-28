"""grupo urls"""

# django
from django.urls import path
from django.contrib.auth.decorators import login_required
#locals
from app.users.decorators import unauthenticated_user,allowed_users,admin_only

# Views
from app.grupos.views import ListaGrupo,ListaGrupoJson,CrearGrupo,EliminarGrupo,EditarGrupo

urlpatterns =[
    path(
        route='',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (ListaGrupo.as_view())
        ),
        name='index'
    ),
    path(
        route='lista-grupo',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaGrupoJson.as_view())),
        name='lista-grupo'
    ),
    path(
        route='crear-grupo',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (CrearGrupo.as_view())
        ),
        name='crear-grupo'
    ),
     path(
        route='editar-grupo/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EditarGrupo.as_view())
        ),
        name='editar-grupo'
    ),
      path(
        route='eliminar-grupo/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EliminarGrupo.as_view())
        ),
        name='eliminar-grupo'
    )
]
