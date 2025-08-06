from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, home, cadastrar_produto, editar_produto

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),      # Deixa as rotas da API em /api/produtos/
    path('', home, name='home'),           # Página inicial com sua interface
    path('cadastrar/', cadastrar_produto, name='cadastrar_produto'),
    path('editar-produto/<int:id>/', editar_produto, name='editar_produto'),
]