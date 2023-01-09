from django.urls import path
from .views import (
    cuenta_nueva_view, pensionados_view, detalle_cuenta_view, admin_cuentas, order, cuenta_editar_view
)
app_name = 'cuentas'
urlpatterns = [
    path('cuenta_nueva/client<int:id>/', cuenta_nueva_view, name='cuenta_nueva'),
    path('', pensionados_view, name='pensionados'),
    path('<int:id>/', detalle_cuenta_view, name='detalle_cuenta'),
    path('admin/<int:id>/', admin_cuentas, name='admin_cuentas'),
    path('admin/orden/', order, name='orden'),
    path('edit/<int:id>/', cuenta_editar_view, name='editar_cuenta'),
]