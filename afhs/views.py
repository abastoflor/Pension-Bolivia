from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from catalogo.models import Tipo, Menu, OrdenMenu
import datetime
import json



def home_view(request):
    today = datetime.date.today()
    menu = Menu.objects.filter(fecha=today)
    context = {
        'menu':menu,
    }
    return render(request, 'home.html', context)



@login_required
@staff_member_required
def hacer_menu(request):
    today = datetime.date.today()
    tipos = Tipo.objects.all()
    try:
        menu = Menu.objects.get(fecha=today)
    except Menu.DoesNotExist:
        menu = None

    context = {
        'tipos': tipos,
        'fecha': today,
        'menu':menu,
    }
    return render(request, 'hacer_menu.html', context)


@login_required
@staff_member_required
def borrar_menu(request, id=None):
    menu = get_object_or_404(Menu, id=id)
    menu.delete()
    return redirect('hacer_menu')


@login_required
@staff_member_required
def ordenMenu(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        menu = Menu.objects.create()

        for tipo_ids in data['tipo_ids']:
            OrdenMenu(tipo=Tipo.objects.get(pk=tipo_ids), menu=menu).save()

        menu.save()
    return redirect('ver_menu')


@login_required
@staff_member_required
def ver_menu(request):
    fecha = datetime.date.today()    
    try:
        menu = Menu.objects.get(fecha=fecha)
        ordenes = menu.ordenmenu_set.all()
    except:
        menu = None
        ordenes = None
   
    context = {
        'menu':menu,
        'ordenes': ordenes,
        'fecha': fecha
    }
    return render(request, 'ver_menu.html', context)