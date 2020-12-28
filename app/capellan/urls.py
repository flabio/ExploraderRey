"""mayor URLs."""
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from app.users.decorators import unauthenticated_user, allowed_users, admin_only

# View
from app.capellan.views import lista_capellan,crear_capellan

urlpatterns = [

    path(
        route='listado-capellan/',
        view=login_required(allowed_users(allowed_roles=['admin'])(lista_capellan.as_view())),
        name='listado-capellan'
    ),

    path(
        route='crear-capellan/<slug:rol>',
        view=login_required(allowed_users(allowed_roles=['admin'])(crear_capellan.as_view())),
        name='crear-capellan'
    ),


    
]
