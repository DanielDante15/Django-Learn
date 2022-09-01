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

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome



class PedidoItem(models.Model):
    
    produto = models.ForeignKey(Produto,on_delete=models.DO_NOTHING)
    preco_un = models.DecimalField(max_digits=6,decimal_places=2)
    qtd = models.SmallIntegerField()
    #pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return str("Item "+str(self.id))

class Pedido(models.Model):
    STATUS_PAGO = 'P'
    STATUS_CANCELADO = 'C'
    STATUS_AGUARDANDO = 'A'

    STATUS_PG = [
        (STATUS_AGUARDANDO,'Aguardando'),
        (STATUS_CANCELADO,'Cancelado'),
        (STATUS_PAGO,'Pago')
    ]
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)
    dt_pedido = models.DateTimeField(auto_now_add=True)
    status_pagamento = models.CharField(max_length=1,choices=STATUS_PG,default=STATUS_AGUARDANDO)

    itens = models.ManyToManyField(PedidoItem)

    def __str__(self) -> str:
        return str("Pedido "+str(self.id))








