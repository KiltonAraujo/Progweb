from django.urls import path
from loja.views.CarrinhoView import create_carrinhoitem_view, list_carrinho_view, confirmar_carrinho_view, incrementar_item_view, decrementar_item_view, remover_item_view
urlpatterns = [
    path("", list_carrinho_view, name='list_carrinho'),
    path("<int:produto_id>", create_carrinhoitem_view, name='create_carrinhoitem'),
    path("confirmar", confirmar_carrinho_view, name='confirmar_carrinho'),
    path('carrinho/incrementar/<int:item_id>/', incrementar_item_view, name='incrementar_item'),
    path('carrinho/decrementar/<int:item_id>/', decrementar_item_view, name='decrementar_item'),
    path('remover/<int:item_id>/', remover_item_view, name='remover_carrinhoitem'),
]