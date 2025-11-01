from django.contrib import admin
from .models import Produto_Cadastro, Usuario, Movimentacao

# Register your models here.
admin.site.register(Produto_Cadastro)
admin.site.register(Usuario)
admin.site.register(Movimentacao)
