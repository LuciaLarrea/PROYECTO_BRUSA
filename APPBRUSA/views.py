from django.shortcuts import render
from APPBRUSA import forms, models

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


# OTRA APP


"""
def cursos(request):
    if request.method == 'POST':
        formulario = forms.Form_Curso(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = models.Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, 'APPBRUSA/cursos.html')
    else:
        formulario = forms.Form_Curso()
        contexto = {"formulario": formulario}
        return render(request, "APPBRUSA/cursos.html", contexto)


def profesores(request):
    return render(request, 'APPBRUSA/profesores.html')


def estudiantes(request):
    return render(request, 'APPBRUSA/estudiantes.html')


def entregables(request):
    return render(request, 'APPBRUSA/entregables.html')


def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = models.Curso.objects.filter(camada__icontains=camada)
        return render(request, 'APPBRUSA/index.html', {'cursos': cursos, "camada": camada})
    else:
        respuesta = 'No enviaste datos'

    return render(request, 'APPBRUSA/index.html', {'respuesta': respuesta})   

def contacto(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        email = request.GET['email']
        asunto = request.GET['asunto']
        mensaje = request.GET['mensaje']

        return render(request, 'APPBRUSA/index.html', {'nombre': nombre, "email": email, "asunto": asunto, "mensaje": mensaje})
    else:
        respuesta = 'No enviaste datos'

    return render(request, 'APPBRUSA/index.html', {'respuesta': respuesta})"""