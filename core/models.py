from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TipoProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "tipo_produto"


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    valor = models.FloatField()
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    texto_longo = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "produto"


class Venda(models.Model):
    data_venda = models.DateTimeField(auto_now_add=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor_venda = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto.nome

    class Meta:
        db_table = "venda"
