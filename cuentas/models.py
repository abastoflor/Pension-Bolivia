from django.db import models
from usuarios.models import Cliente, Usuario
from catalogo.models import Producto


class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_c = models.DateField(auto_now_add=True)
    fecha_m = models.DateField(auto_now=True)
    usuario_c = models.ForeignKey(Usuario, related_name='creador', on_delete=models.CASCADE)
    usuario_m = models.IntegerField(blank=True, null=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    adelanto = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    saldo = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    activo = models.BooleanField(default=True)


    def clean(self):
        self.saldo = self.total - self.adelanto

    def __str__(self):
        return f'{self.cliente.first_name} {self.cliente.last_name}-{self.id}'


class Orden(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.cuenta} - Orden N°: {self.id}'

class OrdenItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    order = models.ForeignKey(Orden, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.producto}-{self.cantidad}'