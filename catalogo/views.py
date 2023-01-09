from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .forms import MarcaForm, UnidadMedidaForm, ProductoForm, TipoForm, CategoriaForm
from .models import UnidadMedida, Marca, Producto, Tipo, Categoria


@login_required
@staff_member_required
def umedida_lista_view(request):
    obj = UnidadMedida.objects.all()
    context = {
        'object_list': obj,
    }
    return render(request, 'catalogo/umedida_lista.html', context)



@login_required
@staff_member_required
def umedida_nueva_view(request):
    form = UnidadMedidaForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/umedida.html', context)



@login_required
@staff_member_required
def umedida_editar_view(request, id=None):
    obj = get_object_or_404(UnidadMedida, id=id)
    form = UnidadMedidaForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj': obj,
        'msg': 'Editar'
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/umedida.html', context)



@login_required
@staff_member_required
def marca_lista_view(request):
    obj = Marca.objects.all()
    context = {
        'object_list': obj,
    }
    return render(request, 'catalogo/marca_lista.html', context)



@login_required
@staff_member_required
def marca_nueva_view(request):
    form = MarcaForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/marca.html', context)


@login_required
@staff_member_required
def marca_editar_view(request, id=None):
    obj = get_object_or_404(Marca, id=id)
    form = MarcaForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj': obj,
        'msg': 'Editar'
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/marca.html', context)


@login_required
@staff_member_required
def producto_lista_view(request):
    obj = Producto.objects.all()
    context = {
        'object_list': obj,
    }
    return render(request, 'catalogo/producto_lista.html', context)


@login_required
@staff_member_required
def producto_nuevo_view(request):
    form = ProductoForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/producto.html', context)


@login_required
@staff_member_required
def producto_editar_view(request, id=None):
    obj = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj': obj,
        'msg': 'Editar'
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/producto.html', context)


@login_required
@staff_member_required
def tipo_lista_view(request):
    obj = Tipo.objects.all()
    context = {
        'object_list': obj,
    }
    return render(request, 'catalogo/tipo_lista.html', context)


@login_required
@staff_member_required
def tipo_nuevo_view(request):
    form = TipoForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/tipo.html', context)


@login_required
@staff_member_required
def tipo_editar_view(request, id=None):
    obj = get_object_or_404(Tipo, id=id)
    form = TipoForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj': obj,
        'msg': 'Editar'
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/tipo.html', context)



@login_required
@staff_member_required
def categoria_lista_view(request):
    obj = Categoria.objects.all()
    context = {
        'object_list': obj,
    }
    return render(request, 'catalogo/categoria_lista.html', context)



@login_required
@staff_member_required
def categoria_nueva_view(request):
    form = CategoriaForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/categoria.html', context)


@login_required
@staff_member_required
def categoria_editar_view(request, id=None):
    obj = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=obj)
    context = {
        'form': form,
        'obj': obj,
        'msg': 'Editar'
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'catalogo/categoria.html', context)


