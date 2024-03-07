from django.test import TestCase
from APPBRUSA.models import Cliente
from django.urls import reverse
from django.contrib.auth import get_user_model

class VerificarRutas(TestCase):
    def test_pagina_inicio(self):
        url = reverse('Inicio')
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 200)

class EliminarClienteTest(TestCase):
    def setUp(self):
        self.Cliente = Cliente.objects.create(nombre="Juan", email="juan@gmail.com")
        user = get_user_model()
        user.objects.create_user('username', password="genericpassword123454321")
    
    def test_setup(self):
        """
        Verificar que creo adecuadamente la instancia de estudiante
        """
        self.assertQuerysetEqual(Cliente.objects.filter(nombre__icontains="Juan", email="juan@gmail.com").values(), 
                                 [{'nombre': 'Juan', 'email': 'juan@gmail.com', 'id': 1}])
    
    def test_login(self):
        """
        Verificar que se inicie sesión
        """
        self.assertTrue(self.client.login(username='username', password='genericpassword123454321'))
    

    def test_eliminar_cliente(self):
        """
        Verificar que se elimine estudiante al iniciar sesión
        """
        self.client.login(username='username', password='genericpassword123454321')
        url = reverse('BorrarCliente', args=[self.Cliente.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Cliente.objects.filter(nombre__icontains="Juan", email__icontains="juan@gmail.com"), 
                                 [])

    def test_no_eliminar_cliente(self):
        """
        Verificar que NO se elimine estudiante sin iniciar sesión
        """
        url = reverse('BorrarCliente', args=[self.Cliente.id])
        respuesta = self.client.post(url)
        self.assertEqual(respuesta.status_code, 302)
        self.assertQuerysetEqual(Cliente.objects.filter(nombre__icontains="Juan", email__icontains="juan@gmail.com").values(), 
                                 [{'nombre': 'Juan', 'email': 'juan@gmail.com', 'id': 1}])