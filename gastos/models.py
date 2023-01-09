from django.db import models
from django.urls import reverse


class Gasto(models.Model):
    motivo = models.CharField(max_length=100)
    salida = models.DecimalField(max_digits=7, decimal_places=2)
    cambio = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    observaciones = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('gastos:lista_gasto')
        

    
class Cambio(models.Model):
    cantidad = models.DecimalField(max_digits=7, decimal_places=2, default=0, help_text='Ingrese la cantidad cuando el cambio haya sido entregado')

    def __str__(self):
        return self.cantidad

    def get_absolute_url(self):
        return reverse('catalogo:marca_lista')