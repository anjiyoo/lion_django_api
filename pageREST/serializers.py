from rest_framework import serializers
from .models import Product

class ProductPagerestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'created_at']