from django.contrib import admin
from .models import Poliza,Auto,Contacto,UserExtension
# Register your models here.

@admin.register(Poliza)
class PolizaAdmin(admin.ModelAdmin):
        list_display = ('nombre','categoria', 'descripcion','precio', 'telefonoContacto', 'emailContacto', 'imagendocumento')
        list_filter = ('nombre', 'categoria', 'descripcion','precio', 'telefonoContacto', 'emailContacto', 'imagendocumento')
        search_fields = ('nombre', 'categoria', 'descripcion','precio', 'telefonoContacto', 'emailContacto', 'imagendocumento')

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
        list_display=("tipo","marca","modelo","anio","color","placa","kilometraje","fotoauto")
        list_filter=("tipo","marca","modelo","anio","color","placa","kilometraje","fotoauto")
        search_fields=("tipo","marca","modelo","anio","color","placa","kilometraje","fotoauto")

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
        list_display=("nombre","email","message","tipocontacto","subs","imagendoc")
        list_filter=("nombre","email","message","tipocontacto","subs","imagendoc")
        search_fields=("nombre","email","message","tipocontacto","subs","imagendoc")

admin.site.register(UserExtension)