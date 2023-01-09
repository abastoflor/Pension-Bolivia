from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _



class Usuario(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=100,)
    last_name = models.CharField(_('last name'), max_length=100,)
    direccion = models.CharField('Dirección', max_length=100, blank=True, null=True)
    telefono = models.CharField('Teléfono', max_length=100, blank=True, null=True)
    
    def clean(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Cliente(Usuario):
    verificado = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    