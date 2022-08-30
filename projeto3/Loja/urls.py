from django.urls import path
from . import views


urlpatterns = [
    path('produtos/', views.produto_listar),
    path('produtos/<int:id>/', views.produto_detalhes),
    
]
