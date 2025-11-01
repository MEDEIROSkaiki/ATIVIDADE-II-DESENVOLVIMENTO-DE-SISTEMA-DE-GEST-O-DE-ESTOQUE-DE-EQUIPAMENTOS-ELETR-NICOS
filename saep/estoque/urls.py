from django.urls import path
from . import views  # Importa as views do app

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    # URLs de Produtos
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/editar/<int:id_produto>/', views.editar_produto, name='editar_produto'),
    # URLs de Movimentações
    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('movimentacoes/adicionar/', views.adicionar_movimentacao, name='adicionar_movimentacao'),
]