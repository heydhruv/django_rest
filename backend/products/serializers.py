from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(
        view_name='product-update',
        lookup_field='pk'
    )
    email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'update_url',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
            'email',
        ]

    def create(self, validated_data): # just to understand create of seri..
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        return obj
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-list", kwargs={"pk": obj.pk}, request=request)