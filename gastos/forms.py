from django import forms
from .models import Gasto, Cambio


class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['salida'].widget.attrs.update({'placeholder': 'Ingrese la cantidad entregada'})
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-user'})


class CambioForm(forms.ModelForm):
    class Meta:
        model = Cambio
        fields = ['cantidad']
    
    def __init__(self, *args, **kwargs):
        super(CambioForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-user'})
