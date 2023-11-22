from django import forms
from .models import Poliza,Auto, Contacto
from django.contrib.auth.forms import  UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class PolizaForm(forms.ModelForm):
    descripcion= forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 1}))
    class Meta:
        model = Poliza
        fields = ['nombre', 'categoria', 'descripcion','precio', 'telefonoContacto', 'emailContacto', 'imagendocumento']



class AutoForm(forms.ModelForm):
    class Meta:
        model= Auto
        fields = ["tipo","marca","modelo","anio","color","placa","kilometraje","fotoauto"]


class FormContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre","email","message","tipocontacto","subs","imagendoc"]



class FormularioRegistroUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
        
        
class Formperfiledit(forms.Form):

    email       = forms.EmailField(required=True, widget=forms.EmailInput(attrs={ 'class' : 'form-control' }))
    first_name  = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }), label='Nombre')
    last_name   = forms.CharField(required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }), label='Apellido')
    avatar      = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={ 'class' : 'form-control' }))
    descripcion = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={  'class' : 'form-control' }))
    link        = forms.URLField(max_length=100, required=False, widget=forms.TextInput(attrs={ 'class' : 'form-control' }))


class FormCambioPassword(PasswordChangeForm):

    old_password  = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Password actual')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Password nuevo')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class' : 'form-control' }), label='Confirmar password')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
