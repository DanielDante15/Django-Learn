from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from Loja.models import Avaliacao, Produto, Cliente, Pedido, PedidoItem
from decimal import Decimal

# class ProdutoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     nome = serializers.CharField(max_length= 255)
#     preco = serializers.DecimalField(max_digits=6,decimal_places=2)
#     preco_tax = serializers.SerializerMethodField(method_name='calcular_taxa')

#     def calcular_taxa(self,produto:Produto):

# return produto.preco * Decimal(1.1)


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'preco_tax',
                  'qtd_estoque', 'categoria', 'descritivo']
        
    def create(self, validated_data):
        if(self.validated_data['qtd_estoque'] < 0 ):

            return super().create(validated_data)

    def update(self, instance, validated_data):
        if(self.validated_data['qtd_estoque'] < 0 ):
            validated_data['qtd_estoque'] = 0
        return super().update(instance, validated_data)

    preco_tax = serializers.SerializerMethodField(method_name='calcular_taxa')

    def calcular_taxa(self, produto: Produto):
        return produto.preco * Decimal(1.1)


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'dt_pedido', 'status_pagamento', 'cliente']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'email', 'data_cadastro']


class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = ['produto', 'preco_un', 'qtd']


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao


        fields = ['id', 'produto','nome','descricao','dt_avaliacao','estrelas']

    def create(self, validated_data):
        if(self.validated_data['estrelas'] > 5 ):
            validated_data['estrelas'] = 5
            return validated_data
        if(self.validated_data['estrelas']<0):
            validated_data['estrelas'] = 0
            return validated_data
