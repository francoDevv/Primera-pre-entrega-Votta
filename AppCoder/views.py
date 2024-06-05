from django.shortcuts import render
from .models import Producto, Clientes, Proveedores, Ventas
from .forms import ProductoFormulario, ClienteFormulario, ProveedorFormulario, VentaFormulario

def lista_productos(req):

  lista = Producto.objects.all()

  return render(req, "lista_productos.html", {"lista_productos": lista})

def inicio(req):

  return render(req, "inicio.html", {})

def productos(req):

  return render(req, "productos.html", {})

def clientes(req):

  return render(req, "clientes.html", {})

def proveedores(req):

  return render(req, "proveedores.html", {})

def ventas(req):

  return render(req, "ventas.html", {})

def producto_formulario(req):

  print('method: ', req.method)
  print('POST: ', req.POST)

  if req.method == 'POST':

    formularioProducto = ProductoFormulario(req.POST)

    if formularioProducto.is_valid():

      data = formularioProducto.cleaned_data

      nuevo_producto = Producto(nombre=data['nombre'], precio=data['precio'], cantidad=data['cantidad'])
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
