from django import forms
from django.contrib.auth.forms import (PasswordChangeForm, UserChangeForm, UserCreationForm)
from .models import Cliente, Usuario


class ClienteForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('first_name', 'last_name', 'direccion', 'telefono', 'email', )

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == 'password1' or field == 'password2':
                self.fields[field].help_text = None
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-user'})


class UpdateClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('id', 'first_name', 'last_name', 'direccion', 'telefono', 'email', 'verificado')

    def __init__(self, *args, **kwargs):
        super(UpdateClienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-user'})



class UsuarioChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = Usuario

    def __init__(self, *args, **kwargs):
        super(UsuarioChangePasswordForm, self).__init__(*args, **kwargs)
        for fieldname in ['new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None



class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'direccion', 'telefono', 'email')

    def __init__(self, *args, **kwargs):
        super(UsuarioChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = ''
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control form-control-user'})