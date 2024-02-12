from django import forms

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


