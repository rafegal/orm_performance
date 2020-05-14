from django.shortcuts import render
from .models import Venda
from django.db.models import F

# Create your views here.


def listagem_vendas(requests):
    """
        Responsável por o template de listagem todas as vendas efetuadas.
        Consulta com performance inferior.
    """
    # É feito a busca de todos os campos, inclusive os que não serão usados.
    # Não é feito join no nomento da consulta, fazendo com que seja criado uma nova consulta
    # para cada item de uma Foreign Key que for acessada.
    vendas = Venda.objects.all()
    return render(requests, "lista_venda.html", {"vendas": vendas})


def listagem_vendas_performance(requests):
    """
        Responsável por o template de listagem todas as vendas efetuadas.
        Consulta com performance superior.
    """

    # É feito a busca de todas as vendas, mas apenas dos campos que serão realmente utilizados.
    # O Join já é realizado com todas as tabelas que forem necessárias ser acessadas
    # evitando assim, mais consultas para cada item de FK que deverá ser acessado.
    vendas = (
        Venda.objects.select_related("produto", "produto__tipo")
        .filter()
        .values("valor_venda", "data_venda")
        .annotate(produto=F("produto__nome"), tipo_produto=F("produto__tipo__nome"))
    )
    return render(requests, "lista_venda_performance.html", {"vendas": vendas})
