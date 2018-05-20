from django.conf.urls import url
from django.urls import path

from .views import  (
    ProductDetailView,
    ProductListView
    )


app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name="list"), #/product/
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"), # /product/1/
]