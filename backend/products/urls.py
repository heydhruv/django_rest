from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailsApiView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view(), name='product-update'),
    path('<int:pk>/delete/', views.ProductDeleteApiView.as_view()),
    path('', views.ProductListCreateApiView.as_view(), name="product-list")
]
