from rest_framework import serializers
from .models import Product, Category, Image

class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
    

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image_url',)


class ProductSerializer(serializers.ModelSerializer):
    categories = CategroySerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'description', 'images', 'categories',)


