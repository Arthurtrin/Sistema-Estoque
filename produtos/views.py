from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer
from django.shortcuts import render

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


def home(request):
    return render(request, 'index.html')

def cadastrar_produto(request):
    return render(request, 'cadastrar-produto.html')


def editar_produto(request, id):
    return render(request, 'editar-produto.html', {'produto_id': id})