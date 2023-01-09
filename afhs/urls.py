from django.contrib import admin
from django.urls import path, include
from .views import home_view, hacer_menu, ordenMenu, ver_menu, borrar_menu


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', home_view, name='home'),
    path('cat/', include('catalogo.urls')),
    path('pension/', include('cuentas.urls')),
    path('pos/', include('ventas.urls')),
    path('ver_menu/', ver_menu, name='ver_menu'),
    path('menu/', hacer_menu, name='hacer_menu'),
    path('ordenMenu/', ordenMenu, name='ordenMenu'),
    path('borrar_menu/<int:id>/', borrar_menu, name='borrar_menu',),
    path('gastos/', include('gastos.urls')),
]