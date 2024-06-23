Link para el archivo de pruebas: https://docs.google.com/spreadsheets/d/1xcaAIshviU0szQwaapdOfv4Bd-FPnwFI/edit?usp=sharing&ouid=116597228210101415654&rtpof=true&sd=true

Link del video explicativo: https://www.youtube.com/watch?v=RhaFTLi9OWY

Hola! Esta aplicación trata de simular lo que sería un sistema que utlizaría una empresa o pyme para el control o manejo de sus productos, como de sus clietes, como de sus proveedores y ventas.
Tenemos 2 urls principales en el proyecto:
- http://127.0.0.1:8000/app-coder/
- http://127.0.0.1:8000/admin/
- 
Dentro de la primera url mencionada encontraremos lo siguiente:
Posee una barra de navegación la cual nos ofrece 6 secciones: (Inicio, Productos, Clientes, Proveedores, Ventas, Sobre Mi), y 2 botones (Ingresar, Registrate).
Cada seccion tiene un metodo GET el cual trae de la base de datos algunos items de prueba para mostrar
Cada sección, sacando el Inicio, tiene 1 url como mínimo cpara buscar algo en especifíco:
Productos :
- http://127.0.0.1:8000/app-coder/busqueda-producto/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de los productos.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-producto/?nombre_del_producto y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que el producto no se encontró en la base de datos.
- Ademas tenemos 4 botones que nos brinda la posibilidad de hacer un CRUD de productos.
- Solo la vista de Productos tiene la opción de tener una vista detallada.

Clientes :
- http://127.0.0.1:8000/app-coder/busqueda-cliente/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de los clientes.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-cliente/?nombre_del_cliente y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que el cliente no se encontró en la base de datos.
- Ademas tenemos 4 botones que nos brinda la posibilidad de hacer un CRUD de clientes.

Proveedores :
- http://127.0.0.1:8000/app-coder/busqueda-proveedor/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de los proveedores.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-proveedor/?razon_social y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que el proveedor no se encontró en la base de datos.
- Ademas tenemos 4 botones que nos brinda la posibilidad de hacer un CRUD de proveedores.

Ventas : 
- http://127.0.0.1:8000/app-coder/busqueda-venta/ => nos muestra una pagina donde mediante un input, nos pide algún dato para realizar una busqueda en la base de datos dentro de las ventas.
  A su vez tenemos un boton de "Buscar" el cual nos dirigirá a http://127.0.0.1:8000/app-coder/buscar-venta/?num_orden y nos realizará la busqueda mediante el valor dado y nos lo mostrará
  en pantalla en caso de que lo encuentre. En caso que no lo encuentre, mostrará un mensaje indicando que la venta no se encontró en la base de datos.
- Ademas tenemos 4 botones que nos brinda la posibilidad de hacer un CRUD de ventas.

Sobre mi:
- Solo tiene un metodo GET al entrar a la sección, que renderiza un HTML con información estática.

Tenemos diferentes funcionalidades dentro de la aplicación web, como editar perfiles, loguearse, registrarse, o agregar avatars que cada una esta definida en el archivo urls. Para la funcion de editar perfiles debemos estar logueados con cualquier perfil, y para la opción de agregar avatar tenemos que tener un usuario administrador. A si mismo, para agregar productos a la base de datos tambien debemos ser administradores.

La url http://127.0.0.1:8000/admin/ nos permite entrar al administrador del proyecto, en el cual encontraremos la base de datos junto a otras configuraciones del proyecto en si.
Las credenciales de acceso son: 
Superusuario por si lo necesitan por algo (en principio no es necesario que lo usen)
Username: francovotta
Password: 123456

Staff user de prueba
Username: usuario_administrador
Password: Administration1234

usuario comun
Username: liomessi
Password: Crack1234


