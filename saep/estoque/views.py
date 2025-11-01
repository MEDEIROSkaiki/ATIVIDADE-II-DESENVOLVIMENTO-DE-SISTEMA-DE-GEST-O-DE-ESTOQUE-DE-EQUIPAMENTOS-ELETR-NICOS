from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto_Cadastro, Movimentacao, Usuario
from django.utils import timezone
from django.contrib import messages

def index(request):
    """Página inicial que serve como um painel."""
    return render(request, 'index.html')

def lista_produtos(request):
    """Exibe todos os produtos cadastrados."""
    produtos = Produto_Cadastro.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def editar_produto(request, id_produto):
    """Permite editar um produto existente."""
    produto = get_object_or_404(Produto_Cadastro, pk=id_produto)
    if request.method == 'POST':
        produto.nome_produto = request.POST['nome_produto']
        produto.limite_produto = request.POST['limite_produto']
        produto.qtd_atual = request.POST['qtd_atual']
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'editar_produto.html', {'produto': produto})

def lista_movimentacoes(request):
    """Exibe todas as movimentações de produtos."""
    movimentacoes = Movimentacao.objects.select_related('id_produto_fk', 'id_usuario_fk').all().order_by('-data_movimentacao')
    return render(request, 'lista_movimentacoes.html', {'movimentacoes': movimentacoes})

def adicionar_movimentacao(request):
    """Adiciona uma nova movimentação de entrada ou saída de produto."""
    produtos = Produto_Cadastro.objects.all()
    
    # NOTA: Como não há um sistema de login, estamos usando o primeiro usuário como padrão.
    # Em um sistema real, você usaria request.user.
    usuario_logado = Usuario.objects.first()

    if request.method == 'POST':
        id_produto = request.POST['produto']
        tipo = request.POST['tipo_movimentacao']
        quantidade = int(request.POST['quantidade'])

        produto = get_object_or_404(Produto_Cadastro, pk=id_produto)

        # Atualiza a quantidade do produto
        if tipo == 'ENTRADA':
            produto.qtd_atual += quantidade
        elif tipo == 'SAIDA':
            produto.qtd_atual -= quantidade
        
        produto.save()

        # Cria o registro da movimentação
        Movimentacao.objects.create(
            id_produto_fk=produto,
            id_usuario_fk=usuario_logado,
            data_movimentacao=timezone.now(),
            entrada_saida=tipo,
            qtd_movimentacao=quantidade
        )

        # Verifica se o estoque está baixo após uma saída
        if tipo == 'SAIDA' and produto.qtd_atual <= produto.limite_produto:
            messages.warning(request, f"Atenção: O produto '{produto.nome_produto}' atingiu o estoque mínimo!")

        return redirect('lista_movimentacoes')

    return render(request, 'adicionar_movimentacao.html', {'produtos': produtos})