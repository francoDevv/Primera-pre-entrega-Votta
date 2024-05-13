from paquete1.modulo1 import *
from paquete1.modulo2 import *

cliente1 = Cliente("Franco", "franco@mail.com", 20, 1000, "abc 123")
cliente1.datos()
cliente1.comprar()
cliente1.pedir_envio()
cliente1.reembolsar()
print(cliente1)