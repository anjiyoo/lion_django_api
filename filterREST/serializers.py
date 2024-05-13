from rest_framework import serializers
from .models import Product

class ProductFilterrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'in_stock', 'created_at']
