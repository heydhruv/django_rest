from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteApiView.as_view()),
    path('', views.ProductMixinView.as_view())
]
