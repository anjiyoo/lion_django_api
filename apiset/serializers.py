# apiset/serializers.py
from rest_framework import serializers
from .models import Product

class ProductApisetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'in_stock']