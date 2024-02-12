from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
import json

@api_view(["POST"])
def home_api(request, *args, **kwargs):

    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        response_data = serializer.save()
    return Response(serializer.data)