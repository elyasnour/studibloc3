from rest_framework import serializers
from catalog.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "category", "price", "discount")