from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename="product")

urlpatterns = router.urls