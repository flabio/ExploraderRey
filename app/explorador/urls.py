
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from app.users.decorators import unauthenticated_user, allowed_users, admin_only

# View
from app.explorador.views import lista_explorador,crear_explorador

urlpatterns = [

    path(
        route='listado-explorador/',
        view=login_required(allowed_users(allowed_roles=['admin'])(lista_explorador.as_view())),
        name='listado-explorador'
    ),
   
path(
        route='crear-explorador/<slug:rol>',
        view=login_required(allowed_users(allowed_roles=['admin'])(crear_explorador.as_view())),
        name='crear-explorador'
    ),
    
]
