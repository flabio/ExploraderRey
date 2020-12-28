"""destacamento urls"""

# django
from django.urls import path
from django.contrib.auth.decorators import login_required
#locals
from app.users.decorators import unauthenticated_user,allowed_users,admin_only

# Views
from app.destacamento.views import ListaDestacamento,ListaDestacamentoJson,ListaGrupoDestacamentoJson,CrearDestacamento,EditarDestacamento,EliminarDestacamento,DestacamentoDetalleView,CrearGrupoDestacamento,EliminarGrupoDestacamento

urlpatterns =[
    path(
        route='',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (ListaDestacamento.as_view())
        ),
        name='index'
    ),
    path(
        route='lista-destacamento',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaDestacamentoJson.as_view())),
        name='lista-destacamento'
    ),
    path(
        route='crear-destacamento',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (CrearDestacamento.as_view())
        ),
        name='crear-destacamento'
    ),
    path(
        route='editar-destacamento/<int:pk>',
        view = login_required(allowed_users(allowed_roles=['admin'])(EditarDestacamento.as_view())),
        name='editar-destacamento'
    ),
    path(
        route='eliminar-destacamento/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EliminarDestacamento.as_view())
        ),
        name='eliminar-destacamento'
    ),
    path(
        route='detalle-destacamento/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (DestacamentoDetalleView.as_view())
        ),
        name='detalle-destacamento'
    )
    ,
    path(
        route='crear-grupo-destacamento',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (CrearGrupoDestacamento.as_view())
        ),
        name='crear-grupo-destacamento'
    ),
    path(
        route='lista-grupo-destacamento/<int:pk>',
        view = login_required(
                allowed_users(allowed_roles=['admin','navegantes']) 
                (ListaGrupoDestacamentoJson.as_view())),
        name='lista-grupo-destacamento'
    )
    ,
    path(
        route='eliminar-grupo-destacamento/<int:pk>',
        view = login_required(
            allowed_users(allowed_roles=['admin'])
            (EliminarGrupoDestacamento.as_view())
        ),
        name='eliminar-grupo-destacamento'
    )
]
