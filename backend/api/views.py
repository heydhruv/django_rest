from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
import json

@api_view(["GET", "POST"])
def home_api(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    else :
        data = None
    return Response(data)