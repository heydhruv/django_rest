from django.urls import path
from .views import SearchListViewAlgolia
urlpatterns =[
    path('', SearchListViewAlgolia.as_view(), name='search')
]