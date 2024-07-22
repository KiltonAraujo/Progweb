from .HomeUrls import *
from .ProdutoUrls import *

from django.urls import path
from loja.views.ProfileView import list_produto_view
urlpatterns = [
    path("", list_produto_view, name='produtos'),
    path("<int:id>", list_produto_view, name='produto'),
]