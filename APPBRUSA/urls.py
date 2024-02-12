"""
URL configuration for Clase10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from APPBRUSA import views

# esto es la estructura de la aplicacion web

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('NosotrosBrusa', views.nosotros_brusa, name="Nosotros Brusa"),
    path('ContactosBrusa', views.contactos_brusa, name="Contactos Brusa"),
    path('NuestrosProductosacondicionador', views.nuestrosproductosacondicionador_brusa, name="Productos Acondicionador Brusa"),
    path('NuestrosProductosshampoo', views.nuestrosproductosshampoo_brusa, name="Productos Shampoo Brusa"),
    path('ResenaBrusa', views.resena_brusa, name="Reseña Brusa")

]