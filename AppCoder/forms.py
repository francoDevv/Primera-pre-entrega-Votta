from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar

class ProductoFormulario(forms.Form):

  nombre = forms.CharField()
  categoria = forms.CharField()
  precio = forms.IntegerField()
  cantidad = forms.IntegerField()
  descripcion = forms.CharField()

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

class EditarPerfilFormulario(UserChangeForm):
  password = forms.CharField(label="Constraseña", widget=forms.PasswordInput)
  passwordConfirmar = forms.CharField(label="Confirmar constraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

  def clean_passwordConfirmar(self):
    
    print(self.cleaned_data)

    password = self.cleaned_data["password"]
    passwordConfirmar = self.cleaned_data["passwordConfirmar"]

    if password != passwordConfirmar:
      raise forms.ValidationError("Las contraseñas no coinciden")
    return password
  
class AvatarFormulario(forms.ModelForm):
  class Meta:
    model = Avatar
    fields = ["imagen"]