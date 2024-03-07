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
from django.contrib.auth.views import LogoutView

# esto es la estructura de la aplicacion web

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('NosotrosBrusa', views.nosotros_brusa, name="Nosotros Brusa"),
    path('ContactosBrusa', views.contactos_brusa, name="Contactos Brusa"),
    path('NuestrosProductosacondicionador', views.nuestrosproductosacondicionador_brusa, name="Productos Acondicionador Brusa"),
    path('NuestrosProductosshampoo', views.nuestrosproductosshampoo_brusa, name="Productos Shampoo Brusa"),
    path('ResenaBrusa', views.resena_brusa, name="Reseña Brusa"),
    path('login', views.login_request,name="Login"),
    path('Logout', LogoutView.as_view(template_name="APPBRUSA/PAGES/logout.html",), name="Logout"),
    path('register', views.register_request,name="Register"),
    path('editar_perfil', views.editarPerfil, name="EditarPerfil"),
    path('cambiarClave', views.CambiarClave.as_view(), name="CambiarClave"),
    path('Cliente/lista', views.ClienteListView.as_view(), name="ListaClientes"),
    path('Cliente/nuevo', views.ClienteCreateView.as_view(), name="NuevoCliente"),
    path('Cliente/<pk>', views.ClienteDetailView.as_view(), name="DetalleCliente"),
    path('Cliente/<pk>/editar', views.ClienteUpdateView.as_view(), name="EditarCliente"),
    path('Cliente/<pk>/borrar', views.ClienteDeleteView.as_view(), name="BorrarCliente"),
        
]