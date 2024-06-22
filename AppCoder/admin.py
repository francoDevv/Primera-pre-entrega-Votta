from django.contrib import admin
from .models import *

class ProductoAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'precio', 'cantidad']
  search_fields = ['nombre']
  list_filter = ['nombre']

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(Ventas)
admin.site.register(Avatar)

