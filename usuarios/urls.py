from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (registrar_cliente_view,
                    editar_cliente_view,
                    UsuarioChangePasswordView,
                    editar_usuario_view,
                    detalle_cliente_view
)

app_name = 'usuarios'
urlpatterns = [
    path('registro/', registrar_cliente_view, name='registro_cliente'),
    path('editar/usuario/', editar_usuario_view, name='editar_usuario'),
    path('editar/password/', UsuarioChangePasswordView.as_view(), name='editar_pass_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('cliente/<int:id>/editar/', editar_cliente_view, name='editar_cliente'),
    path('det/<int:id>/', detalle_cliente_view, name='detalle_cliente'),
]