from django.db import models
from django.contrib.auth.models import User

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} {self.email} | {self.asunto} | {self.mensaje} "

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} | {self.email}"

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre}| ARS {self.precio}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
