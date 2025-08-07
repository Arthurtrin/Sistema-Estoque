from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

def home(request):
    return render(request, 'index.html')

def cadastrar_produto(request):
    return render(request, 'cadastrar-produto.html')

def editar_produto(request, id):
    return render(request, 'editar-produto.html', {'produto_id': id})

def consultar_produtos(request):
    return render(request, 'consulta-produtos.html')


@api_view(['POST'])
def api_cadastrar_produto(request):
    serializer = ProdutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'mensagem': 'Produto salvo com sucesso!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_produto(request, id_produto):
    try:
        produto = Produto.objects.get(id=id_produto)
    except Produto.DoesNotExist:
        return Response({'erro': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProdutoSerializer(produto, data=request.data)
    if serializer.is_valid():
        # Verifica se há alterações reais
        atualizou = False
        for campo, novo_valor in serializer.validated_data.items():
            valor_antigo = getattr(produto, campo)
            if valor_antigo != novo_valor:
                atualizou = True
                break

        if atualizou:
            serializer.save()
            return Response({'mensagem': 'Produto atualizado com sucesso!'})
        else:
            return Response({'mensagem': 'Nenhuma alteração detectada.'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def excluir_produto(request, id_produto):
    try:
        produto = Produto.objects.get(id=id_produto)
    except Produto.DoesNotExist:
        return Response({'erro': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    produto.delete()
    return Response({'mensagem': 'Produto excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)



