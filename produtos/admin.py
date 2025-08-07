from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields = ('preco_total',)  # campo visível, mas não editável

    # Se quiser que apareça nas colunas da listagem também:
    list_display = ('nome', 'quantidade', 'preco_unitario', 'preco_total', 'prateleira')

