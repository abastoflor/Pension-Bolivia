from django import forms
from .models import UnidadMedida, Marca, Producto, Tipo, Categoria, OrdenMenu, Menu

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre',]

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre'})
            self.fields[field].widget.attrs.update({'class':'form-control'})



class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['nombre', 'categoria']

    def __init__(self, *args, **kwargs):
        super(UnidadMedidaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre'})
            self.fields[field].widget.attrs.update({'class':'form-control'})


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', ]

    def __init__(self, *args, **kwargs):
        super(MarcaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre'})
            self.fields[field].widget.attrs.update({'class':'form-control'})


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'medida', 'marca', 'precio' ]

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre'})
            self.fields[field].widget.attrs.update({'class':'form-control'})


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre', 'producto', ]

    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['nombre'].widget.attrs.update({'placeholder': 'Nombre'})
            self.fields[field].widget.attrs.update({'class':'form-control'})



