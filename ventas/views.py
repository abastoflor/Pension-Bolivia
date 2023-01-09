from django.shortcuts import render, redirect
from catalogo.models import Producto
from .models import Venta, OrdenVenta
import json
import datetime

def pos(request):
    productos = Producto.objects.all()
    ventas = Venta.objects.all()
    if ventas:
        ventas= Venta.objects.latest('id')
        print(ventas)
    context = {
        'productos': productos,
        'ventas': ventas,
    }
    return render(request, 'ventas/pos.html', context)


def orden(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        venta = Venta.objects.create(gran_total=data['precio_total'],)

        for producto_id in data['producto_ids']:
            OrdenVenta(producto=Producto.objects.get(pk=producto_id), venta=venta).save()

        venta.save()
    return redirect('ventas:pos')



def ventasTotal(request):
    ventas = Venta.objects.all()
    orden_ventas = OrdenVenta.objects.filter(fecha=datetime.date.today())
    total = 0
    for i in ventas:
        if i.fecha_c == datetime.date.today():
            total += i.gran_total
    context = {
        'ventas':ventas,
        'orden_ventas':orden_ventas,
        'total': total,
    }
    return render(request, 'ventas/ventas.html', context)