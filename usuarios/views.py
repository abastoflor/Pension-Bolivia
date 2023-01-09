from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ClienteForm, UpdateClienteForm, UsuarioChangePasswordForm, UsuarioChangeForm
from .models import Usuario, Cliente


@login_required
@staff_member_required
def registrar_cliente_view(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        form.instance.username = fn.replace(' ','').lower() + ln[:3].replace(' ', '').lower()
        form.save()
        return redirect('cuentas:pensionados')
    return render(request, 'registration/registro_cliente.html', {'form': form})



@login_required
@staff_member_required
def editar_cliente_view(request, id=None):
    obj = get_object_or_404(Cliente, id=id)
    form = UpdateClienteForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('cuentas:pensionados')
    return render(request, 'registration/editar_cliente.html', {'form': form, 'obj': obj})


@login_required
@staff_member_required
def detalle_cliente_view(request, id=None):
    obj = get_object_or_404(Cliente, id=id)
    activas = list(obj.cuenta_set.filter(activo=True).values_list('id', flat=True))
    inactivas = list(obj.cuenta_set.filter(activo=False).values_list('id', flat=True))
    context = {
        'obj': obj,
        'activas': enumerate(activas, start=1),
        'inactivas': enumerate(inactivas, start=1),
        }
    return render(request, 'registration/detalle_cliente.html', context)



class UsuarioChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = UsuarioChangePasswordForm
    template_name = 'registration/usuario_change_pass.html'
    success_url = reverse_lazy('home')



def editar_usuario_view(request):
    obj = get_object_or_404(Usuario, username=request.user.username)
    form = UsuarioChangeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'registration/editar.html', {'form': form, 'obj': obj})