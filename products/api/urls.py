from django.conf.urls import url
from django.urls import path

from .views import  (
    ProductDetailAPIView,
    ProductListAPIView,
    ProductFeaturedListAPIView,
    ProductSlugAPIView
    )


app_name = 'products-api'

urlpatterns = [
    path('', ProductListAPIView.as_view(), name="list"), # /api/product/
    path('featured/', ProductFeaturedListAPIView.as_view(), name="featured"), # /api/product/featured
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="detail"), # /api/product/1/
    path('<str:slug>/', ProductSlugAPIView.as_view(), name="detail"), # /api/product/slug/ --> for Admin Page

]


