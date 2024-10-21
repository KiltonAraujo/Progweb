from django.urls import path
from loja.views.UsuarioView import *

urlpatterns = [
    path("", list_usuario_view, name='usuario'),
    path("edit", edit_usuario_view, name='edit_usuario'),
]