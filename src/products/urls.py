from django.conf.urls import url
from django.urls import path

from .views import  (
    ProductDetailView,
    ProductListView,
    SearchProductListView
    )


app_name = 'products'

urlpatterns = [
    path('search/', SearchProductListView.as_view(), name="search-list"), #/product/
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"), # /product/1/
]