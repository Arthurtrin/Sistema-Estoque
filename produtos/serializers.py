from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

    def create(self, validated_data):
        quantidade = validated_data.get('quantidade')
        preco_unitario = validated_data.get('preco_unitario')
        validated_data['preco_total'] = quantidade * preco_unitario
        return Produto.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.descricao = validated_data.get('descricao', instance.descricao)
        instance.quantidade = validated_data.get('quantidade', instance.quantidade)
        instance.preco_unitario = validated_data.get('preco_unitario', instance.preco_unitario)
        instance.prateleira = validated_data.get('prateleira', instance.prateleira)

        # Tratamento automático: calcular o preco_total
        instance.preco_total = instance.quantidade * instance.preco_unitario

        instance.save()
        return instance