"""explorodar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from app.dashboard import views as inicio

# from app.users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio.ListaDashboard),
    # path('users/login/', users_views.login_view,name="login"),
    # path('users/logout/', users_views.logout_view,name="logout"),
    #path('/',include(('app.users.urls','users'), namespace='users')),
    path('dashboard/', include(('app.dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('estudiorealizado/', include(('app.estudiorealizado.urls', 'estudiorealizado'), namespace='estudiorealizado')),
    path('nivelministerial/', include(('app.nivelministerial.urls', 'nivelministerial'), namespace='nivelministerial')),
    path('iglesia/', include(('app.iglesia.urls', 'iglesia'), namespace='iglesia')),
    path('destacamento/',include(('app.destacamento.urls','destacamento'),namespace='destacamento')),
    path('grupos/',include(('app.grupos.urls','grupos'),namespace='grupos')),
    path('eps/',include(('app.eps.urls','eps'),namespace='eps')),
    path('patrulla/',include(('app.patrulla.urls','patrulla'),namespace='patrulla')),
    path('users/',include(('app.users.urls','users'), namespace='users')),
    path('administrador/',include(('app.administrador.urls','administrador'), namespace='administrador')),
    path('mayor/',include(('app.mayor.urls','mayor'), namespace='mayor')),
    path('capellan/',include(('app.capellan.urls','capellan'), namespace='capellan')),
    path('comandante/',include(('app.comandante.urls','comandante'), namespace='comandante')),
    path('explorador/',include(('app.explorador.urls','explorador'), namespace='explorador')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
