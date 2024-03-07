from django.shortcuts import render
from APPBRUSA import forms, models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy



# CAPA DE CONTROLLERS
def inicio(request):
    return render(request, 'APPBRUSA/PAGES/index.html')

def nosotros_brusa(request):
    return render(request, 'APPBRUSA/PAGES/NosotrosBrusa.html')

def contactos_brusa(request):
    if request.method == 'POST': #el usuario mando un formulario de contacto
        formulario = forms.Form_Contacto(request.POST)
        if formulario.is_valid(): #el formulario es valido
            print(formulario.cleaned_data)
            informacion = formulario.cleaned_data
            contacto_model = models.Contacto(nombre=informacion["nombre"], email=informacion["email"], asunto=informacion["asunto"], mensaje=informacion["mensaje"])
            contacto_model.save()
            contexto = {"formulario": forms.Form_Contacto()}
            return render(request, 'APPBRUSA/PAGES/ContactosBrusa.html', contexto)
        else: #formulario tiene errores
            contexto = {"formulario": formulario}
            return render(request, 'APPBRUSA/PAGES/ContactosBrusa.html', contexto)
    else: #el usuario accede a la pagina
        contexto = {"formulario": forms.Form_Contacto()}
        return render(request, 'APPBRUSA/PAGES/ContactosBrusa.html', contexto)

def nuestrosproductosacondicionador_brusa(request):
    return render(request, 'APPBRUSA/PAGES/NuestrosProductosacondicionador.html')

def nuestrosproductosshampoo_brusa(request):
    if request.method == 'POST': #el usuario mando un formulario de producto(ALTA de producto)
        formulario = forms.Form_Producto(request.POST)
        if formulario.is_valid(): #el formulario es valido
            informacion = formulario.cleaned_data
            producto_model = models.Producto(nombre=informacion["nombre"], precio=informacion["precio"])
            producto_model.save()
            contexto = {"formulario": forms.Form_Cliente(), "formulario_busqueda": forms.Form_Producto()}
            return render(request, 'APPBRUSA/PAGES/NuestrosProductosshampoo.html')
    else: #es un GET, busqueda o ir a la pagina por primera vez
        if 'nombre' in request.GET: #el usuario hace una busqueda
            nombre = request.GET['nombre']
            if nombre:
                productos = models.Producto.objects.filter(nombre__icontains=nombre)
                formulario = forms.Form_Producto()
                formulario_busqueda = forms.Form_Producto()
                filter_busqueda = {"nombre": nombre}
                return render(request, 'APPBRUSA/PAGES/NuestrosProductosshampoo.html',
                              {
                                  "busqueda": True,
                                  "productos": productos,
                                  "nombre": nombre,
                                  "formulario_busqueda": formulario_busqueda,
                                  "formulario": formulario,
                                  "filter_busqueda": filter_busqueda
                              })
            else:
                formulario = forms.Form_Producto()
                formulario_busqueda = forms.Form_Producto()
                return render(request, 'APPBRUSA/PAGES/NuestrosProductosshampoo.html',
                              {
                                  "busqueda": True,
                                  "formulario_busqueda": formulario_busqueda,
                                  "formulario": formulario
                              })
        else: #render pagina primera vez
            return render(request, 'APPBRUSA/PAGES/NuestrosProductosshampoo.html', {"formulario": forms.Form_Producto(), "formulario_busqueda": forms.Form_Producto()})

def resena_brusa(request):
    if request.method == 'POST': #el usuario mando un formulario de contacto
        formulario = forms.Form_Cliente(request.POST)
        if formulario.is_valid(): #el formulario es valido
            informacion = formulario.cleaned_data
            cliente_model = models.Cliente(nombre=informacion["nombre"], email=informacion["email"])
            cliente_model.save()
            contexto = {"formulario": forms.Form_Cliente()}
            return render(request, 'APPBRUSA/PAGES/ResenaBrusa.html', contexto)
        else: #formulario tiene errores
            contexto = {"formulario": formulario}
            return render(request, 'APPBRUSA/PAGES/ResenaBrusa.html', contexto)
    else: #el usuario accede a la pagina
        contexto = {"formulario": forms.Form_Contacto()}
        return render(request, 'APPBRUSA/PAGES/ResenaBrusa.html', contexto)


def login_request(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
        
            if form.is_valid():
                # Si pasó la validación de Django
                usuario = form.cleaned_data.get('username')
                contrasenia = form.cleaned_data.get('password')
                user = authenticate(username= usuario, password=contrasenia)
                login(request, user)            
                return render(request, "APPBRUSA/PAGES/index.html", {"mensaje": f'Bienvenide {user.username}'})            
        else:
            form = AuthenticationForm()
        
        return render(request, "APPBRUSA/PAGES/login.html", {"form": form})

    
# Vista de registro
def register_request(request):
      if request.method == 'POST':
            form = forms.Form_Registro(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"APPBRUSA/PAGES/index.html", {"mensaje": f'Bienvenido {username}'})
      else:
            form = forms.Form_Registro()     
      return render(request,"APPBRUSA/PAGES/register.html" ,  {"form":form})
  
  # Vista para editar perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    models.Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request, "APPBRUSA/PAGES/index.html")
    else:
        miFormulario = forms.UserEditForm(instance=request.user)
    return render(request, "APPBRUSA/PAGES/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = 'APPBRUSA/PAGES/cambiar_clave.html'
    success_url = reverse_lazy('EditarPerfil')
    
# CRUD
# List views
class ClienteListView(ListView):
    model = models.Cliente
    context_object_name = "Clientes"
    template_name = "APPBRUSA/PAGES/cliente_lista.html"
    
class ClienteDetailView(DetailView):
    model = models.Cliente
    template_name = "APPBRUSA/PAGES/cliente_detalle.html"
      
class ClienteCreateView(PermissionRequiredMixin, CreateView):
    model = models.Cliente 
    permission_required = "user.is_superuser"
    template_name = "APPBRUSA/PAGES/cliente_crear.html"
    success_url = reverse_lazy('ListaClientes')
    fields = ['nombre', 'email']
    raise_exception = True
        
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Cliente
    template_name = "APPBRUSA/PAGES/cliente_editar.html"
    success_url = reverse_lazy('ListaClientes')
    fields = ['nombre', 'email']

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Cliente
    template_name = "APPBRUSA/PAGES/cliente_borrar.html"
    success_url = reverse_lazy('ListaClientes')


