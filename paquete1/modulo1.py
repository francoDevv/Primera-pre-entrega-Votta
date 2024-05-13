class Cliente:

    def __init__(self, nombre, email, edad, presupuesto, direccion):
        self.nombre = nombre
        self.email = email
        self.edad = int(edad)
        self.presupuesto = int(presupuesto)
        self.direccion = direccion

    def datos(self):
        print(f"Datos de {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Edad: {self.edad}")
        print(f"Presupuesto: ${self.presupuesto}")
        print(f"Direccion: {self.direccion}")

    def comprar(self):
        producto = input("Ingresa que producto queres comprar:")
        self.producto = producto
        precio_producto = int(input("Ingresa el valor del producto: "))
        self.precio_producto = precio_producto
        if (self.presupuesto < precio_producto):
            print(f"El presupuesto no alcanza para comprar {producto}")
        else:
            presupuesto_actualizado = self.presupuesto - precio_producto
            self.presupuesto_actualizado = presupuesto_actualizado
            print(f"Producto adquirido, el nuevo presupuesto es: ${self.presupuesto_actualizado}")
            print(f"La factura se enviará al mail {self.email}")

    def pedir_envio(self):
        transporte = input("Ingresa el transporte por el cual quieres recibir el producto, en caso de no querer envío, responder con un no: ")
        transporte_capitalizado = transporte.capitalize()
        if (transporte_capitalizado == "No"):
            print(f"{self.nombre} tenes que retirar tu {self.producto} por nuestra sucursal.")
        else:
            print(f"{self.nombre} recibirás tu {self.producto} en {self.direccion} por el transporte {transporte_capitalizado}.")

    def reembolsar(self):
        confirmacion = input(f"{self.nombre} estas seguro que deseas reembolsar tu compra de {self.producto}? Responde con si o no: ")
        confirmacion_capitalizado = confirmacion.capitalize()
        if (confirmacion_capitalizado == "No"):
            print(f"Nos alegra que conserves tu {self.producto}")
            print(f"Tu presupuseto sigue siendo: ${self.presupuesto_actualizado}")
        else:
            print(f"{self.producto} fue reembolsado, tu nuevo presupuesto es: ${self.presupuesto_actualizado + self.precio_producto}")

    def __str__(self):
        return(f"Soy un cliente llamado/a {self.nombre} con el email {self.email} y tengo {self.edad} años. Mi presupuesto inicial es ${self.presupuesto} y vivo en {self.direccion}")
        

