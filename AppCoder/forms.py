from django import forms

class ProductoFormulario(forms.Form):

  nombre = forms.CharField()
  precio = forms.IntegerField()
  cantidad = forms.IntegerField()

class ClienteFormulario(forms.Form):

  nombre = forms.CharField()
  apellido = forms.CharField()
  email = forms.EmailField()

class ProveedorFormulario(forms.Form):

  razon_social = forms.CharField()
  email = forms.EmailField()
  cuil = forms.IntegerField()

class VentaFormulario(forms.Form):

  num_orden = forms.IntegerField()
  fecha_venta = forms.DateField()
  entregado = forms.BooleanField()