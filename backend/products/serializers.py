from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title
class ProductSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(
        view_name='product-update',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validate_title])
    class Meta:
        model = Product
        fields = [
            'update_url',
            'url',
            'title',
            'content',
            'price',
            'sale_price',
        ]

    # def create(self, validated_data): # just to understand create of seri..
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-list", kwargs={"pk": obj.pk}, request=request)