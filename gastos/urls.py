from django.urls import path
from .views import gasto_nuevo, gasto_editar, lista_gastos

app_name = 'gastos'

urlpatterns = [
    path('', gasto_nuevo, name='gasto_nuevo'),
    path('<int:id>/', gasto_editar, name='gasto_editar'),
    path('lista/', lista_gastos, name='lista_gasto'),
]