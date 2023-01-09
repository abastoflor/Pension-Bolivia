from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Cambio, Gasto
from .forms import GastoForm, CambioForm

@login_required
@staff_member_required
def gasto_nuevo(request):
    form = GastoForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'gastos/gasto_nuevo.html', context)


@login_required
@staff_member_required
def gasto_editar(request, id=None):
    obj = get_object_or_404(Gasto, id=id)
    form = GastoForm(request.POST or None, instance=obj)
    context = {
        'form':form,
        'obj':obj,
        'msg':'Editar',
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, 'gastos/gasto_nuevo.html', context)



@login_required
@staff_member_required
def lista_gastos(request):
    object_list = Gasto.objects.all()
    context = {
        'object_list':object_list,
    }
    return render(request, 'gastos/lista_gastos.html', context)