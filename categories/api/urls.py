from django.conf.urls import url
from django.urls import path

from .views import  (
    CategoryDetailAPIView,
    CategoryListAPIView,
    ProductListByCategoryAPIView,
    )


app_name = 'categories-api'

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name="list"), # /api/category/
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name="detail"), # /api/category/1/
    path('<int:pk>/product/', ProductListByCategoryAPIView.as_view(), name="product-detail"), # /api/category/1/product
]