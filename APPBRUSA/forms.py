from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from django.contrib.auth.models import User

class Form_Contacto(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.EmailField()
    asunto = forms.CharField(max_length=20)
    mensaje = forms.CharField(max_length=100)

class Form_Cliente(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.EmailField()
 

class Form_Producto(forms.Form):
    nombre = forms.CharField(max_length=20)
    precio = forms.IntegerField()

class Form_Registro(UserCreationForm):
    username = forms.TextInput()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel   
        fields = ['username','email','password1','password2'] 
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)
    
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']