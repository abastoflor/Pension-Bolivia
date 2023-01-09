from django.urls import path
from .views import pos, orden, ventasTotal



app_name = 'ventas'
urlpatterns = [
    path('', pos, name='pos'),
    path('orden/', orden, name='orden'),
    path('ventas/', ventasTotal, name='ventas'),
]