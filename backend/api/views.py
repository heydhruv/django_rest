from django.http import JsonResponse
from products.models import Product
import json
def home_api(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data= {}
    if model_data:
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
    return JsonResponse(data)