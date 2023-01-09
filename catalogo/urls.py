from django.urls import path
from .views import (
    categoria_lista_view, categoria_nueva_view, categoria_editar_view,
    marca_lista_view, marca_nueva_view, marca_editar_view,
    umedida_lista_view, umedida_nueva_view, umedida_editar_view,
    producto_lista_view, producto_nuevo_view, producto_editar_view,
    tipo_lista_view, tipo_nuevo_view, tipo_editar_view
)

app_name = 'catalogo'
urlpatterns = [
    path('categorias/', categoria_lista_view, name='categoria_lista'),
    path('categoria/nueva/', categoria_nueva_view, name='categoria_nueva'),
    path('categoria/<int:id>/', categoria_editar_view, name='categoria_editar'),
    path('marcas/', marca_lista_view, name='marca_lista'),
    path('marca/nueva/', marca_nueva_view, name='marca_nueva'),
    path('marca/<int:id>/', marca_editar_view, name='marca_editar'),
    path('umedidas/', umedida_lista_view, name='umedida_lista'),
    path('umedida/nueva/', umedida_nueva_view, name='umedida_nueva'),
    path('umedida/<int:id>/', umedida_editar_view, name='umedida_editar'),
    path('productos/', producto_lista_view, name='producto_lista'),
    path('producto/nuevo/', producto_nuevo_view, name='producto_nuevo'),
    path('producto/<int:id>/', producto_editar_view, name='producto_editar'),
    path('tipos/', tipo_lista_view, name='tipo_lista'),
    path('tipo/nuevo/', tipo_nuevo_view, name='tipo_nuevo'),
    path('tipo/<int:id>/', tipo_editar_view, name='tipo_editar'),
    
]