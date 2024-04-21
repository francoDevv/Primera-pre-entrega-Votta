def registrar_usuario(): #Funcion para registrar usuario
    usuario = input("Ingrese nombre de usuario: ")
    if usuario in base_de_datos_usuarios:
        print("El usuario ya existe. Por favor, elige otro nombre de usuario.")
        return
    contraseña = input("Ingrese contraseña: ")
    base_de_datos_usuarios[usuario] = contraseña
    print("Usuario registrado exitosamente.")

def mostrar_usuarios(): #Funcion para mostrar usuarios
    if not base_de_datos_usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for usuario, contraseña in base_de_datos_usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")

def iniciar_sesion(): #Funcion para iniciar sesion con los usuarios ya registrados
    if not base_de_datos_usuarios:
        print("No hay usuarios registrados, por favor registra uno.")
        return
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if usuario in base_de_datos_usuarios and base_de_datos_usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
    else:
        print("Credenciales incorrectas.")

def salir_del_menu(): #Funcion para salir del menu
    print("Hasta luego.")

#Diccionario para almacenar los usuarios
base_de_datos_usuarios = {}

def mostrar_menu(): #Función para mostrar el menú
    while True:
        print("\nMenú:")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar todos los usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir del menú")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            iniciar_sesion()
        elif opcion == "4":
            salir_del_menu()
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

mostrar_menu() #Ejecutar el menú
