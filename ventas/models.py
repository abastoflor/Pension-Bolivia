from django.db import models
from catalogo.models import Producto
from django.utils import timezone


class Venta(models.Model):
    fecha_c = models.DateField(auto_now_add=True)
    gran_total = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        ordering = ['-fecha_c']



class OrdenVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ['fecha']




