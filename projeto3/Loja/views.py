import re
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto
from .serializer import ProdutoSerializer
from rest_framework import status

@api_view(['GET','POST'])
def produto_listar(request):
    if request.method == 'GET':

        queryset = Produto.objects.all()
        serializer = ProdutoSerializer(queryset,many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response('ok')

@api_view()
def produto_detalhes(request,id):

    # try:
        produto = get_object_or_404(Produto, pk=id) 
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)
    # except:
    #     return Response(status= status.HTTP_404_NOT_FOUND)