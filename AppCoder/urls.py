from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name='Inicio'), 
    path('productos/', lista_productos, name='Productos'), 
    path('clientes/', lista_clientes, name='Clientes'), 
    path('proveedores/',lista_proveedores, name='Proveedores'), 
    path('ventas/', lista_ventas, name='Ventas'),
    path('sobre_mi/', sobre_mi, name='SobreMi'),  
    path('producto-formulario/', producto_formulario, name='ProductoFormulario'), 
    path('busqueda-producto/', busqueda_producto, name='BusquedaProducto'), 
    path('buscar-producto/', buscar_producto, name='BuscarProducto'), 
    path('editar-producto/<int:id>', editar_producto, name='EditaProducto'),
    path('eliminar-producto/<pk>', ProductoEliminar.as_view(), name='EliminaProducto'),
    path('detalle-producto/<pk>', ProductoDetalle.as_view(), name = 'DetalleProducto'),
    path('cliente-formulario/', cliente_formulario, name='ClienteFormulario'), 
    path('busqueda-cliente/', busqueda_cliente, name='BusquedaCliente'), 
    path('buscar-cliente/', buscar_cliente, name='BuscarCliente'),
    path('editar-cliente/<int:id>', editar_cliente, name='EditaCliente'),
    path('eliminar-cliente/<int:id>', eliminar_cliente, name='EliminaCliente'), 
    path('proveedor-formulario/', proveedor_formulario, name='ProveedorFormulario'), 
    path('busqueda-proveedor/', busqueda_proveedor, name='BusquedaProveedor'), 
    path('buscar-proveedor/', buscar_proveedor, name='BuscarProveedor'), 
    path('editar-proveedor/<int:id>', editar_proveedor, name='EditaProveedor'),
    path('eliminar-proveedor/<int:id>', eliminar_proveedor, name='EliminaProveedor'),
    path('venta-formulario/', venta_formulario, name='VentaFormulario'), 
    path('busqueda-venta/', busqueda_venta, name='BusquedaVenta'), 
    path('buscar-venta/', buscar_venta, name='BuscarVenta'), 
    path('editar-venta/<int:id>', editar_venta, name='EditaVenta'),
    path('eliminar-venta/<int:id>', eliminar_venta, name='EliminaVenta'),
    path('login/', login_view, name = 'Login'),
    path('registrar/', registro, name = 'Registrar'),
    path('logout/', LogoutView.as_view(template_name = "logout.html"), name = 'Logout'),
    path('editar-perfil/', editar_perfil, name = 'EditaPerfil'),
    path('agregar-avatar/', agregar_avatar, name = 'AgregarAvatar')
]
