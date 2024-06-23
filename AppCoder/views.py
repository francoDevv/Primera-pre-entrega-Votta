from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

def inicio(req):
  try:
    avatar = Avatar.objects.get(usuario = req.user.id)   
    return render(req, "inicio.html", {"url": avatar.imagen.url})
  except:
    return render(req, "inicio.html")

def sobre_mi(req):

  return render(req, "sobre_mi.html", {})

def lista_productos(req):

  lista_productos = Producto.objects.all()

  return render(req, "productos.html", {"lista_productos": lista_productos})

def lista_clientes(req):

  cliente = Clientes.objects.all()

  return render(req, "clientes.html", {"lista_clientes": cliente})

def lista_proveedores(req):

  proveedores = Proveedores.objects.all()

  return render(req, "proveedores.html", {"lista_proveedores": proveedores})

def lista_ventas(req):

  ventas = Ventas.objects.all()

  return render(req, "ventas.html", {"lista_ventas": ventas})

# @staff_member_required(login_url="/app-coder/login")
def producto_formulario(req):
  if req.method == 'POST':

    formularioProducto = ProductoFormulario(req.POST)

    if formularioProducto.is_valid():

      data = formularioProducto.cleaned_data

      nuevo_producto = Producto(nombre=data['nombre'], categoria=data['categoria'], precio=data['precio'], cantidad=data['cantidad'], descripcion=data['descripcion'])
      nuevo_producto.save()

      return render(req, "inicio.html", {"message": "Producto creado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    formularioProducto = ProductoFormulario()

    return render(req, "producto_formulario.html", {"formularioProducto": formularioProducto})


def busqueda_producto(req):

    return render(req, "busqueda_producto.html", {})

def buscar_producto(req):

  if req.GET["nombre"]:

    nombre = req.GET["nombre"]

    productos = Producto.objects.filter(nombre__icontains=nombre)

    return render(req, "resultadoBusquedaProductos.html", {"productos":productos, "nombre": nombre})

  else:
      
      return render(req, "inicio.html", {"message": "No envias el dato del nombre"})

@login_required() 
def editar_producto(req, id):
  if req.method == 'POST':

    formularioProducto = ProductoFormulario(req.POST)

    if formularioProducto.is_valid():

      data = formularioProducto.cleaned_data

      producto = Producto.objects.get(id = id)

      producto.nombre = data["nombre"]
      producto.categoria = data["categoria"]
      producto.precio = data["precio"]
      producto.cantidad = data["cantidad"]
      producto.descripcion = data["descripcion"]

      producto.save()

      return render(req, "inicio.html", {"message": "Producto actualizado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:
    producto = Producto.objects.get(id = id)

    formularioProducto = ProductoFormulario(initial={
      "nombre": producto.nombre,
      "categoria": producto.categoria,
      "precio": producto.precio,
      "cantidad": producto.cantidad,
      "descripcion": producto.descripcion
    })

    return render(req, "producto_editar.html", {"formularioProducto": formularioProducto, "id" : producto.id})
  
class ProductoDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "producto_detalle.html"
    context_object_name = "producto"

class ProductoEliminar(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'producto_eliminar.html'
    success_url = "/app-coder/productos/"
    context_object_name = 'producto'

@login_required() 
def cliente_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    formularioCliente = ClienteFormulario(req.POST)

    if formularioCliente.is_valid():

      data = formularioCliente.cleaned_data

      nuevo_cliente = Clientes(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
      nuevo_cliente.save()

      return render(req, "inicio.html", {"message": "Cliente creado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    formularioCliente = ClienteFormulario()

    return render(req, "cliente_formulario.html", {"formularioCliente": formularioCliente})

def busqueda_cliente(req):

    return render(req, "busqueda_cliente.html", {})

def buscar_cliente(req):

  if req.GET["nombre"]:

    nombre = req.GET["nombre"]

    clientes = Clientes.objects.filter(nombre__icontains=nombre)

    return render(req, "resultadoBusquedaClientes.html", {"clientes":clientes, "nombre": nombre})

  else:
      
      return render(req, "inicio.html", {"message": "No envias el dato del nombre"})
  
@login_required()  
def editar_cliente(req, id):
  if req.method == 'POST':

    formularioCliente = ClienteFormulario(req.POST)

    if formularioCliente.is_valid():

      data = formularioCliente.cleaned_data

      cliente = Clientes.objects.get(id = id)

      cliente.nombre = data["nombre"]
      cliente.apellido = data["apellido"]
      cliente.email = data["email"]

      cliente.save()

      return render(req, "inicio.html", {"message": "Cliente actualizado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:
    cliente = Clientes.objects.get(id = id)

    formularioCliente = ClienteFormulario(initial={
      "nombre": cliente.nombre,
      "apellido": cliente.apellido,
      "email": cliente.email,
    })

    return render(req, "cliente_editar.html", {"formularioCliente": formularioCliente, "id" : cliente.id})
  
@login_required()   
def eliminar_cliente(req, id):
  if req.method == "POST":
    cliente = Clientes.objects.get(id = id)
    cliente.delete()

  lista_clientes = Clientes.objects.all()
  return render(req, "clientes.html", {"lista_clientes": lista_clientes})

@login_required() 
def proveedor_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    formularioProveedor = ProveedorFormulario(req.POST)

    if formularioProveedor.is_valid():

      data = formularioProveedor.cleaned_data

      nuevo_proveedor = Proveedores(razon_social=data['razon_social'], email=data['email'], cuil=data['cuil'])
      nuevo_proveedor.save()

      return render(req, "inicio.html", {"message": "Proveedor cargado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    formularioProveedor = ProveedorFormulario()

    return render(req, "proveedor_formulario.html", {"formularioProveedor": formularioProveedor})

def busqueda_proveedor(req):

    return render(req, "busqueda_proveedor.html", {})

def buscar_proveedor(req):

  if req.GET["razon_social"]:

    razon_social = req.GET["razon_social"]

    proveedores = Proveedores.objects.filter(razon_social__icontains=razon_social)

    return render(req, "resultadoBusquedaProveedores.html", {"proveedores":proveedores, "razon_social": razon_social})

  else:
      
      return render(req, "inicio.html", {"message": "No envias el dato de la razon_social"})

@login_required()   
def editar_proveedor(req, id):
  if req.method == 'POST':

    formularioProveedor = ProveedorFormulario(req.POST)

    if formularioProveedor.is_valid():

      data = formularioProveedor.cleaned_data

      proveedor = Proveedores.objects.get(id = id)

      proveedor.razon_social = data["razon_social"]
      proveedor.email = data["email"]
      proveedor.cuil = data["cuil"]

      proveedor.save()

      return render(req, "inicio.html", {"message": "Proveedor actualizado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:
    proveedor = Proveedores.objects.get(id = id)

    formularioProveedor = ProveedorFormulario(initial={
      "razon_social": proveedor.razon_social,
      "email": proveedor.email,
      "cuil": proveedor.cuil,
    })

    return render(req, "proveedor_editar.html", {"formularioProveedor": formularioProveedor, "id" : proveedor.id})

@login_required()   
def eliminar_proveedor(req, id):
  if req.method == "POST":
    proveedor = Proveedores.objects.get(id = id)
    proveedor.delete()

  lista_proveedores = Proveedores.objects.all()
  return render(req, "proveedores.html", {"lista_proveedores": lista_proveedores})

@login_required() 
def venta_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    formularioVenta = VentaFormulario(req.POST)

    if formularioVenta.is_valid():

      data = formularioVenta.cleaned_data

      nuevo_venta = Ventas(num_orden=data['num_orden'], fecha_venta=data['fecha_venta'], entregado=data['entregado'])
      nuevo_venta.save()

      return render(req, "inicio.html", {"message": "Venta cargada con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    formularioVenta = VentaFormulario()

    return render(req, "venta_formulario.html", {"formularioVenta": formularioVenta})

def busqueda_venta(req):

    return render(req, "busqueda_venta.html", {})

def buscar_venta(req):

  if req.GET["num_orden"]:

    num_orden = req.GET["num_orden"]

    ventas = Ventas.objects.filter(num_orden__icontains=num_orden)

    return render(req, "resultadoBusquedaVentas.html", {"ventas":ventas, "num_orden": num_orden})

  else:
      
      return render(req, "inicio.html", {"message": "No envias el dato del numero de orden"})

@login_required()   
def editar_venta(req, id):
  if req.method == 'POST':

    formularioVenta = VentaFormulario(req.POST)

    if formularioVenta.is_valid():

      data = formularioVenta.cleaned_data

      venta = Ventas.objects.get(id = id)

      venta.num_orden = data["num_orden"]
      venta.fecha_venta = data["fecha_venta"]
      venta.entregado = data["entregado"]

      venta.save()

      return render(req, "inicio.html", {"message": "Venta actualizado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:
    venta = Ventas.objects.get(id = id)

    formularioVenta = VentaFormulario(initial={
      "num_orden": venta.num_orden,
      "fecha_venta": venta.fecha_venta,
      "entregado": venta.entregado,
    })

    return render(req, "venta_editar.html", {"formularioVenta": formularioVenta, "id" : venta.id})

@login_required()   
def eliminar_venta(req, id):
  if req.method == "POST":
    venta = Ventas.objects.get(id = id)
    venta.delete()

  lista_ventas = Ventas.objects.all()
  return render(req, "ventas.html", {"lista_ventas": lista_ventas})

def login_view(req):
  if req.method == 'POST':

    formularioLogin = AuthenticationForm(req, data = req.POST)

    if formularioLogin.is_valid():

      data = formularioLogin.cleaned_data

      nombre_usuario = data["username"]
      contrasena = data["password"]

      usuario = authenticate(username = nombre_usuario, password = contrasena)

      if usuario:
        login(req, usuario)
        return render(req, "inicio.html", {"message": f"Bienvenido {nombre_usuario}"})
      
      else:
        return render(req, "inicio.html", {"message": "Credenciales incorrectas"})
        
    else:
      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    formularioLogin = AuthenticationForm()

    return render(req, "login.html", {"formularioLogin": formularioLogin})
  
def registro(req):
  if req.method == 'POST':

    formularioRegistro = RegistrarFormulario(req.POST)

    if formularioRegistro.is_valid():

      data = formularioRegistro.cleaned_data

      nombre_usuario = data["username"]
      formularioRegistro.save()
      
      return render(req, "inicio.html", {"message":f"Usuario {nombre_usuario} registrado con éxito!"})
        
    else:
      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:

    formularioRegistro = RegistrarFormulario()

    return render(req, "registro.html", {"formularioRegistro": formularioRegistro})

@login_required()   
def editar_perfil(req):
  usuario = req.user

  if req.method == 'POST':

    formularioPerfil = EditarPerfilFormulario(req.POST, instance = req.user)

    if formularioPerfil.is_valid():

      data = formularioPerfil.cleaned_data

      usuario.first_name = data["first_name"]
      usuario.last_name = data["last_name"]
      usuario.email = data["email"]
      usuario.set_password(data["password"])

      usuario.save()

      return render(req, "inicio.html", {"message": "Perfil actualizado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Datos inválidos"})
  
  else:
    formularioPerfil = EditarPerfilFormulario(instance = req.user)

    return render(req, "editar_perfil.html", {"formularioPerfil": formularioPerfil})
  
staff_member_required(login_url="/app-coder/login")   
def agregar_avatar(req):
  usuario = req.user

  if req.method == 'POST':

    formularioAvatar = AvatarFormulario(req.POST, req.FILES)

    if formularioAvatar.is_valid():

      data = formularioAvatar.cleaned_data

      avatar = Avatar(usuario = req.user, imagen = data["imagen"])

      avatar.save()

      return render(req, "inicio.html", {"message": "Avatar actualizado con éxito"})
    
    else:

      return render(req, "inicio.html", {"message": "Error al cargar el avatar"})
  
  else:
    formularioAvatar = AvatarFormulario(instance = req.user)

    return render(req, "agregar_avatar.html", {"formularioAvatar": formularioAvatar})