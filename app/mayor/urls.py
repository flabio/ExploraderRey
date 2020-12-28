"""mayor URLs."""
# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from app.users.decorators import unauthenticated_user, allowed_users, admin_only

# View
from app.mayor.views import ListaMayor,crear_mayor

urlpatterns = [

    path(
        route='listado-mayor/',
        view=login_required(allowed_users(allowed_roles=['admin'])(ListaMayor.as_view())),
        name='listado-mayor'
    ),

    path(
        route='crear-mayor/<slug:rol>',
        view=login_required(allowed_users(allowed_roles=['admin'])(crear_mayor.as_view())),
        name='crear-mayor'
    ),


    
]
