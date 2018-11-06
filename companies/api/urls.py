from django.conf.urls import url
from django.urls import path

from .views import (
    CompanyListAPIView,
    CompanyDetailAPIView,
    ProductListByCategoryAPIView
    )


app_name = 'categories'

urlpatterns = [
    path('', CompanyListAPIView.as_view(), name="list"),  # /company/
    path('<int:pk>/', CompanyDetailAPIView.as_view(), name="detail"),  # /company/pk
    path('<int:pk>/product/', ProductListByCategoryAPIView.as_view(), name="detail"),  # /company/pk/product
]