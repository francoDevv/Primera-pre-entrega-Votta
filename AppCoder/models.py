from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):

  nombre = models.CharField(max_length=40)
  categoria = models.CharField(max_length=40)
  precio = models.IntegerField()
  cantidad = models.IntegerField()
  descripcion = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.nombre} - {self.precio} - {self.cantidad}'
  
  class Meta():

    verbose_name = 'Productos'
    verbose_name_plural = 'Productos'
    ordering = ('nombre', 'precio', 'cantidad')
    unique_together = ('nombre', 'precio', 'cantidad')

class Clientes(models.Model):

  nombre = models.CharField(max_length=30)
  apellido = models.CharField(max_length=30)
  email = models.EmailField(null=True)

  def __str__(self):
    return f'{self.nombre} - {self.apellido}'
  
  class Meta():

    verbose_name = 'Clientes'
    verbose_name_plural = 'Clientes'
    ordering = ('nombre', 'apellido', 'email')
    unique_together = ('nombre', 'apellido', 'email')

class Proveedores(models.Model):

  razon_social = models.CharField(max_length=30)
  email = models.EmailField()
  cuil = models.IntegerField()

  class Meta():

    verbose_name = 'Proveedores'
    verbose_name_plural = 'Proveedores'
    ordering = ('razon_social', 'email', 'cuil')
    unique_together = ('razon_social', 'email', 'cuil')

  def __str__(self):
    return f'{self.razon_social} - {self.email} - {self.cuil}'

class Ventas(models.Model):

  num_orden = models.IntegerField()
  fecha_venta = models.DateField()
  entregado = models.BooleanField()
  
  class Meta():

    verbose_name = 'Ventas'
    verbose_name_plural = 'Ventas'
    ordering = ('num_orden', 'fecha_venta', 'entregado')
    unique_together = ('num_orden', 'fecha_venta', 'entregado')

  def __str__(self):
    return f'{self.num_orden} - {self.fecha_venta} - {self.entregado}'
  
class Avatar(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

# class RegistrarUsuario(models.Model):
#   username = models.CharField(max_length=30) 
#   password = models.CharField(max_length=30)
#   passwordConfirm = models.CharField(max_length=30)
#   email = models.EmailField()