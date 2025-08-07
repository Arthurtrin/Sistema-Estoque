from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, home, cadastrar_produto, editar_produto, api_cadastrar_produto, atualizar_produto, excluir_produto, consultar_produtos

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('cadastrar', cadastrar_produto, name='cadastrar_produto'),
    path('api/produtos/cadastro', api_cadastrar_produto, name='api_produto'),
    path('editar/produto/<int:id>/', editar_produto, name='editar_produto'),
    path('api/editar-produto/<int:id_produto>', atualizar_produto, name='editar_produto_api'),
    path('excluir-produto/<int:id_produto>', excluir_produto, name='excluir_produto'),
    path('consultar/produtos', consultar_produtos, name='consultar_produtos'),

]