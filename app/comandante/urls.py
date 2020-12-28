
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from app.users.decorators import unauthenticated_user, allowed_users, admin_only

# View
from app.comandante.views import lista_comandante,crear_comandante

urlpatterns = [

    path(
        route='listado-comandante/',
        view=login_required(allowed_users(allowed_roles=['admin'])(lista_comandante.as_view())),
        name='listado-comandante'
    ),
   
path(
        route='crear-comandante/<slug:rol>',
        view=login_required(allowed_users(allowed_roles=['admin'])(crear_comandante.as_view())),
        name='crear-comandante'
    ),
    
]
