from pyexpat import model
from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.categoria



class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=True)
    descritivo = models.TextField()
    preco = models.DecimalField(max_digits=6,decimal_places=2)
    qtd_estoque = models.PositiveSmallIntegerField()
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nome

