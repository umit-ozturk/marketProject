from django.conf.urls import url
from django.urls import path

from .views import  (
    ProductDetailAPIView,
    ProductListAPIView,
    ProductFeaturedListAPIView,
    ProductCategoriesListAPIView
    )


app_name = 'products-api'

urlpatterns = [
    path('', ProductListAPIView.as_view(), name="list"), # /api/product/
    path('featured/', ProductFeaturedListAPIView.as_view(), name="featured"), # /api/product/featured
	path('compare/category/', ProductCategoriesListAPIView.as_view(), name="for-category"), # /api/product/compare/category/
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="detail"), # /api/product/1/
    #/api/product/header/category/
    #/api/product/compare/category/
]


