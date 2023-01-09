from django import forms
from .models import Cuenta



class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['cliente', 'total', 'adelanto', 'saldo', 'activo', ]

    def __init__(self, *args, **kwargs):
        super(CuentaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control form-control-user'})
            self.fields['cliente'].widget.attrs.update({'hidden':'hidden'})
            self.fields['cliente'].label = False




class CuentaEditForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['cliente', 'total', 'adelanto', 'saldo', 'activo',]

    def __init__(self, *args, **kwargs):
        super(CuentaEditForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['cliente'].widget.attrs['disabled'] = 'disabled'
            self.fields[field].widget.attrs.update({'class':'form-control'})