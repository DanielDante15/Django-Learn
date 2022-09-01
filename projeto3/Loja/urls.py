from django.urls import path
from . import views


urlpatterns = [
    path('produtos/', views.produto_listar),
    path('produtos/<int:id>/', views.produto_detalhes),
    path('clientes/', views.cliente_listar),
    path('clientes/<int:id>/', views.cliente_detalhes),
    path('pedidos/', views.pedido_listar),
    path('pedidos/<int:id>/', views.pedido_detalhes),
    path('items_pedidos/', views.pedido_item_listar),
    path('items_pedidos/<int:id>/', views.pedido_item_detalhes),
    
]
