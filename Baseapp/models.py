from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Poliza(models.Model):
    tipopoliza = (
    ('vida','Vida'),
    ('auto', 'Auto'),
    ('viaje','Viaje'),
    ('empresarial','Empresarial'),
    ('casa','Casa'),
    ('mascota','Mascota'),
    )
    nombre = models.CharField(max_length=45)
    categoria = models.CharField(max_length=15, choices=tipopoliza, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefonoContacto = models.IntegerField(null=True)
    emailContacto = models.EmailField(max_length=45, null=True)
    imagendocumento = models.ImageField(null=True, blank=True, upload_to="contactos/")


class Auto(models.Model):
    tipoauto = (
    ('sedan','Sedan'),
    ('Pick-up', 'Pick-up'),
    ('camion','Camion'),
    ('moto','Moto'),
    ('tractor','Tractor'),
    ('plataforma','Plataforma'),
    )
    tipo=models.CharField(max_length=15,choices=tipoauto,default="Sedan")
    emailauto=models.CharField(max_length=50, verbose_name= "Email")
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=40)
    anio= models.IntegerField(null=True, verbose_name="Año")
    color= models.CharField(max_length=20)
    placa= models.CharField(max_length=30)
    kilometraje=models.IntegerField(null=True)
    fotoauto = models.ImageField(null=True, blank=True, upload_to="autos/",verbose_name="Foto Del Vehiculo")



opciones = [[0,"Pedido de Informacion"],
            [1,"Consultoria de Polizas"],
            [2,"Presupuesto"],
            ]
class Contacto(models.Model):
    nombre = models.CharField(max_length= 100,verbose_name= "Nombre y Apellido")
    email = models.EmailField(verbose_name="Correo electronico")
    message = RichTextField(blank=True,verbose_name= "Cartelera de Mensaje")
    imagendoc = models.ImageField(upload_to="img/",null=True, verbose_name="Cargue su Documento")
    tipocontacto = models.IntegerField(choices= opciones, verbose_name= "Tipo de Contacto")
    subs = models.BooleanField(blank=True,default= False, verbose_name="Subscribete a Correos informativos mensuales")
    
    def __str__(self):
        return self.nombre

class UserExtension(models.Model):

    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255, null=True)
    link        = models.URLField(max_length=100, null=True)
    avatar      = models.ImageField(upload_to='avatares/', null=True, blank=True)
