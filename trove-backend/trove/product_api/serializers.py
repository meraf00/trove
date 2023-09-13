from rest_framework import serializers
from .models import Product, Category

class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    categories = CategroySerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'image_url', 'categories',)