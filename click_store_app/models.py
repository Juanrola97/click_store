from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=30)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.IntegerField()
    correo = models.CharField(max_length=200)

class Cliente(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=30)
    correo = models.CharField(max_length=200)

class Vendedor(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=30)
    correo = models.CharField(max_length=200)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    cantidad = models.IntegerField()

class Carrito(models.Model):
    descripcion = models.CharField(max_length=200)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

class Pedido(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    direccion = models.CharField(max_length=200)
