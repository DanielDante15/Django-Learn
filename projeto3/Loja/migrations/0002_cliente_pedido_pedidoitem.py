# Generated by Django 4.1 on 2022-09-01 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_pedido', models.DateTimeField(auto_now_add=True)),
                ('status_pagamento', models.CharField(choices=[('A', 'Aguardando'), ('C', 'Cancelado'), ('P', 'Pago')], default='A', max_length=1)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Loja.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_un', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd', models.SmallIntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Loja.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Loja.produto')),
            ],
        ),
    ]
