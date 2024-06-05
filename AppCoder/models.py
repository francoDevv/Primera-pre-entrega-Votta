from django.db import models

# Create your models here.
class Producto(models.Model):

  nombre = models.CharField(max_length=40)
  precio = models.IntegerField()
  cantidad = models.IntegerField()

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