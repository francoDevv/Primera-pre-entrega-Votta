Hola! Esta aplicación trata de simular lo que sería un sistema que utlizaría una empresa o pyme para el control o manejo de sus productos, como de sus clietes, como de sus proveedores y ventas.
Tenemos 2 urls principales en el proyecto:
- http://127.0.0.1:8000/app-coder/
- http://127.0.0.1:8000/admin/
- 
Dentro de la primera url mencionada encontraremos lo siguiente:
Posee una barra de navegación la cual nos ofrece 5 secciones: (Inicio, Productos, Clientes, Proveedores, Ventas)
Por el momento estas secciones no presentan información alguna pero ya están conectadas para algún uso futuro.
Cada sección, sacando el Inicio, tiene 3 urls como mínimo con las cuales podemos interactuar:
Productos :
- http://127.0.0.1:8000/app-coder/lista-productos/ => nos traerá todos los productos cargados en la base de datos
- http://127.0.0.1:8000/app-coder/producto-formulario/ => nos mostrará un formulario para cargar un nuevo producto en la base de datos
- http://127.0.0.1:8000/app-coder/busqueda-producto/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de los productos.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-producto/?nombre_del_producto y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que el producto no se encontró en la base de datos.

Clientes :
- http://127.0.0.1:8000/app-coder/cliente-formulario/ => nos mostrará un formulario para cargar un nuevo cliente en la base de datos
- http://127.0.0.1:8000/app-coder/busqueda-cliente/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de los clientes.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-cliente/?nombre_del_cliente y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que el cliente no se encontró en la base de datos.

Proveedores :
- http://127.0.0.1:8000/app-coder/proveedor-formulario/ => nos mostrará un formulario para cargar un nuevo proveedor en la base de datos
- http://127.0.0.1:8000/app-coder/busqueda-proveedor/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de los proveedores.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-proveedor/?razon_social y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que el proveedor no se encontró en la base de datos.

Ventas : 
- http://127.0.0.1:8000/app-coder/venta-formulario/ => nos mostrará un formulario para cargar una nueva venta en la base de datos
- http://127.0.0.1:8000/app-coder/busqueda-venta/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de las ventas.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-venta/?num_orden y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que la venta no se encontró en la base de datos.

Se recomienda que antes de pedir algun dato de la base de datos, se cargue algun producto, cliente, proveedor o venta para asegurarnos que hay si o si, un dato para traer de la misma.

La url http://127.0.0.1:8000/admin/ nos permite entrar al administrador del proyecto, en el cual encontraremos la base de datos junto a otras configuraciones del proyecto en si.
Las credenciales de acceso son: 
Username: francovotta
Password: 123456


