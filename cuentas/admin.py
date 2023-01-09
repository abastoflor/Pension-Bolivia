from django.contrib import admin

from .models import Cuenta, Orden, OrdenItem

admin.site.register(Cuenta)
admin.site.register(Orden)
admin.site.register(OrdenItem)