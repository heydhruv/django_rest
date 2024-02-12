from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailsApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductListApiView(generics.ListAPIView):
""" Not using cuz Listcreateview does it both"""

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
