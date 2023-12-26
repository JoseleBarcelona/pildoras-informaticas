from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name='dirección Empresa')
    email=models.EmailField()
    telefono=models.CharField(max_length=9)

    def __str__(self):
        return self.nombre #el método __str__() devuelve un string y no un objeto en el panel admin

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'Nombre: %s, Sección: %s y Precio %s' % (self.nombre, self.seccion, self.precio) 

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
