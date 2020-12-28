"""Users URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required
from  app.users.decorators import unauthenticated_user, allowed_users, admin_only

# View

from app.users.views import LoginView,LogoutView,EliminarUsers,lista_users_json,crear_user,editar_user

urlpatterns = [

    path(route='login/',view = LoginView.as_view(),name='login'),
    path(route='logout/',view=login_required(LogoutView.as_view()),name='logout'),
    path(route='lista-usersjson/<slug:valor>',view  = login_required(allowed_users(allowed_roles=['admin']) (lista_users_json.as_view())),name  = 'eliminar-users'),
    path(route='crear-user/',view  = login_required(allowed_users(allowed_roles=['admin'])(crear_user.as_view())),name  = 'crear-user' ),
    path(route='editar-user/<int:pk>/<slug:rol>/',view  = login_required(allowed_users(allowed_roles=['admin']) (editar_user.as_view())),name  = 'editar-user'),
    
    path(route='eliminar-users/<int:pk>',view  = login_required(allowed_users(allowed_roles=['admin']) (EliminarUsers.as_view())),name  = 'eliminar-users')
    
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