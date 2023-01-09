from django.db import models
from django.urls import reverse
from django.utils import timezone



class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        self.nombre = self.nombre.title()

    def get_absolute_url(self):
        return reverse('catalogo:categoria_lista')



class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    def clean(self):
        self.nombre = self.nombre.title()

    def get_absolute_url(self):
        return reverse('catalogo:umedida_lista')



class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        self.nombre = self.nombre.title()

    def get_absolute_url(self):
        return reverse('catalogo:marca_lista')



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}-{self.medida}-{self.marca}-{self.precio}'

    def clean(self):
        self.nombre = self.nombre.title()

    class Meta:
        unique_together = ('nombre', 'medida', 'marca', 'precio' )
        ordering = ['-precio']

    def get_absolute_url(self):
        return reverse('catalogo:producto_lista')



class Tipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto}-{self.nombre}'

    def clean(self):
        self.nombre = self.nombre.title()

    def get_absolute_url(self):
        return reverse('catalogo:tipo_lista')

    class Meta:
        ordering = ['producto']



class Menu(models.Model):
    fecha = models.DateField(default=timezone.now, unique=True)

    def __str__(self):
        return f'{self.fecha}'



class OrdenMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.fecha}/{self.id}-{self.menu.id}'

    class Meta:
        ordering = ['-tipo']