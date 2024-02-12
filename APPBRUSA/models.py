from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()