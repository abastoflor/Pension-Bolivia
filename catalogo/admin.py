from django.contrib import admin

from .models import Menu, OrdenMenu, Categoria, Marca, Producto, UnidadMedida, Tipo

admin.site.register(Menu)
admin.site.register(OrdenMenu)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Tipo)



