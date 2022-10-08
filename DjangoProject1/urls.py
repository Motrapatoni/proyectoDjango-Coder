"""DjangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import hola, dia_de_hoy, nombre, vista_template, post_person, get_persons

urlpatterns = [
    path('hola/', hola),
    path('crear/<str:name>/<str:lastname>/<str:email>/', post_person),
    path('mostrar/', get_persons),
    path('dia/', dia_de_hoy),
    path('nombre/<nombre>/', nombre),
    path('api/', vista_template),
    path('admin/', admin.site.urls),
]
