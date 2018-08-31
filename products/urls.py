from django.conf.urls import url
from django.urls import path
from django.conf.urls import include

from .views import  (
    ProductDetailView,
    ProductListView, # --> home.html
    SearchProductListView
    )


app_name = 'products'

urlpatterns = [
    path('search/', SearchProductListView.as_view(), name="search-list"), #/product/
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"), # /product/1/
]