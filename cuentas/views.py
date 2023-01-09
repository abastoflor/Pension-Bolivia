from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CuentaForm, CuentaEditForm
from usuarios.models import Cliente
from cuentas.models import Cuenta, Orden, OrdenItem
from catalogo.models import Producto
import json
import datetime


@login_required
@staff_member_required
def cuenta_editar_view(request, id=None):
    obj = get_object_or_404(Cuenta, id=id)
    form = CuentaEditForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj': obj,
        'msg': 'Corregir usuario_modifica'
    }
    if form.is_valid():
        obj = form.save(commit=False)
        form.instance.usuario_m = request.user.id
        obj.save()
        return redirect('cuentas:pensionados')
    return render(request, 'cuentas/control_cuenta_crear_editar.html', context)


@login_required
@staff_member_required
def cuenta_nueva_view(request, id=None):
    cliente = Cliente.objects.get(id=id)
    form = CuentaForm(request.POST or None, initial={'cliente':cliente})
    context = {
        'cliente': cliente,
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        form.instance.usuario_c = request.user
        obj.save()
        return redirect('cuentas:pensionados')
    return render(request, 'cuentas/control_cuenta_crear_editar.html', context)


@login_required
@staff_member_required
def detalle_cuenta_view(request, id=None):
    cuenta = get_object_or_404(Cuenta, id=id)
    ordenes = Orden.objects.filter(cuenta=cuenta)
    ordenitem = [OrdenItem.objects.filter(order__id=i.id) for i in ordenes]
    productos = [(x.producto.nombre, x.cantidad) for i in ordenitem for x in i]
    productos_total = {}
    counter = 0
    for x in productos:
        counter += x[1]
        if x[0] not in productos_total:
            productos_total[x[0]] = x[1]
        else:
            productos_total[x[0]] = counter
    context = {
        'cuenta': cuenta,
        'ordenes':ordenes,
        'ordenitem': ordenitem,
        'productos_total': productos_total,
        'fecha': datetime.date.today()
    }
    return render(request, 'cuentas/detalle_cuenta.html', context)


@login_required
@staff_member_required
def pensionados_view(request):
    clientes = Cliente.objects.all()
    activas = {}
    for i in clientes:
        activas[i] = (list(i.cuenta_set.filter(activo=True).values_list('id', flat=True)))

    context = {
        'activas': activas,
    }
    if request.user.is_staff:
        return render(request, 'cuentas/pensionados.html', context)
    return render(request, 'home.html', {})


@login_required
@staff_member_required
def admin_cuentas(request, id=None):
    cuenta = get_object_or_404(Cuenta, id=id)
    productos = Producto.objects.all()

    context = {
        'cuenta': cuenta,
        'productos': productos,
    }
    return render(request, 'cuentas/admin_cuentas.html', context)


@login_required
@staff_member_required
def order(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        cuenta = Cuenta.objects.get(pk=data['cuenta_id'])
        order = Orden.objects.create(cuenta=cuenta)

        for product_id, cantidad in data['id_cantidades'].items():
            OrdenItem(producto=Producto.objects.get(pk=product_id), cantidad=cantidad, order=order).save()
        order.save()
    return redirect('cuentas:detalle_cuenta', id=cuenta.id)