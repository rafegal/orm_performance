from django.contrib import admin
from .models import Produto, Venda, TipoProduto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'valor', 'tipo', 'ativo']


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'produto', 'usuario', 'data_venda', 'valor_venda']


@admin.register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome',]