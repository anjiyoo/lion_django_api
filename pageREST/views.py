from rest_framework import viewsets
from .models import Product
from .serializers import ProductPagerestSerializer
from rest_framework.pagination import PageNumberPagination  # 페이지네이션 관련 기능

class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductPagerestSerializer
    pagination_class = ProductPagination