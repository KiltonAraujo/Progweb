from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Carrinho, CarrinhoItem, Usuario
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def create_carrinhoitem_view(request, produto_id=None):
    print('create_carrinhoitem_view')
    produto = get_object_or_404(Produto, pk=produto_id)
    
    if produto:
        print(f'Produto: {produto.id}')
        carrinho_id = request.session.get('carrinho_id')
        print(f'Carrinho ID: {carrinho_id}')

        if carrinho_id:
            carrinho = Carrinho.objects.filter(id=carrinho_id).first()
            print(f'Carrinho encontrado: {carrinho}')

            if carrinho:
                hoje = datetime.today().date()
                if carrinho.criado_em.date() != hoje:
                    carrinho = Carrinho.objects.create()
                    request.session['carrinho_id'] = carrinho.id
                    print(f'Novo carrinho criado: {carrinho.id}')
        else:
            carrinho = Carrinho.objects.create()
            request.session['carrinho_id'] = carrinho.id
            print(f'Carrinho criado: {carrinho.id}')

        carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho, produto=produto).first()
        
        if carrinho_item:
            carrinho_item.quantidade += 1
            print(f'Produto já no carrinho, aumentou a quantidade para {carrinho_item.quantidade}')
        else:
            carrinho_item = CarrinhoItem.objects.create(
                carrinho=carrinho,
                produto=produto,
                quantidade=1,
                preco=produto.preco
            )
            print(f'Novo item adicionado ao carrinho: {carrinho_item.id}')

        carrinho_item.save()
        print(f'Item do carrinho salvo: {carrinho_item.id}')

    return redirect('/carrinho')

def list_carrinho_view(request):
    print('list_carrinho_view')

    carrinho = None
    carrinho_item = None
    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()

        if carrinho:
            print(f'Carrinho encontrado: {carrinho.id}')
            print(f'Data do carrinho: {carrinho.criado_em}')
            carrinho_item = CarrinhoItem.objects.filter(carrinho=carrinho)
            print(f'Itens no carrinho: {carrinho_item}')

    context = {
        'carrinho': carrinho,
        'itens': carrinho_item
    }
    return render(request, 'carrinho/carrinho-listar.html', context=context)

@login_required
def confirmar_carrinho_view(request):
    print ('confirmar_carrinho_view')
    carrinho = None
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id:
        print ('carrinho: ' + str(carrinho_id))
        carrinho = Carrinho.objects.filter(id=carrinho_id).first()
        usuario = get_object_or_404(Usuario, user=request.user)
        print ('Usuario: ' + str(usuario))
    if usuario:
        carrinho.user_id = usuario.id
        carrinho.situacao = 1
        carrinho.confirmado_em = timezone.make_aware(datetime.today())
        carrinho.save()
        print ('carrinho salvo')

    CarrinhoItem.objects.filter(carrinho=carrinho).delete()
    context = {
    'carrinho': carrinho
    }
    return render(request, 'carrinho/carrinho-confirmado.html', context=context)

def remover_item_view(request, item_id):
    item = get_object_or_404(CarrinhoItem, id=item_id)
    # Verifica se o item pertence ao carrinho do usuário (opcional)
    carrinho_id = request.session.get('carrinho_id')
    if carrinho_id == item.carrinho.id:
        item.delete()
    return redirect('/carrinho')