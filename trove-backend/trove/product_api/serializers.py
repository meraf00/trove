from rest_framework import serializers
from .models import Product, Category, Image


class CategroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image_url",)


class ProductSerializer(serializers.ModelSerializer):
    categories = CategroySerializer(many=True)
    images = ImageSerializer(many=True)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "stock",
            "description",
            "images",
            "categories",
        )

    def create(self, validated_data):
        categories = validated_data.pop("categories")
        images = validated_data.pop("images")

        c = []
        for category in categories:
            c.append(Category.objects.get(name=category["name"]))

        img = []
        for image in images:
            img.append(Image.objects.get(name=image["url"]))

        instance = Product.objects.create(**validated_data)

        instance.categories.set(c)
        instance.images.set(img)

        instance.save()

        return instance

    def update(self, instance, validated_data):
        categories = validated_data.pop("categories")
        images = validated_data.pop("images")

        c = []
        for category in categories:
            c.append(Category.objects.get(name=category["name"]))

        img = []
        for image in images:
            img.append(Image.objects.get(name=image["url"]))

        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.description = validated_data.get(
            "description", instance.description
        )

        instance.categories.set(c)
        instance.images.set(img)

        instance.save()

        return instance