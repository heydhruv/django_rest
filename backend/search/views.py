from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from . import client
from rest_framework.response import Response
class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('query')
        if query is not None:
            return qs.search(query)

class SearchListViewAlgolia(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        if not query:
            return Response("", status=404)
        results = client.perform_search(query)
        return Response(results)