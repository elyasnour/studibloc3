from rest_framework import generics, permissions
from catalog.models import Product
from .serializers import ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)  # new
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
