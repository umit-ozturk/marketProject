from django.urls import path
from api.v1.views import *


app_name = 'api'

urlpatterns = [
    #  Aktuel
    path('aktuel/', AktuelListAPIView.as_view(), name="list"),  # /api/aktuel/
    path('aktuel/<int:pk>/', AktuelDetailAPIView.as_view(), name="detail"),  # /api/aktuel/id/

    #  Category
    path('category/', CategoryListAPIView.as_view(), name="list"),  # /api/category/
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name="detail"),  # /api/category/1/
    path('category/<int:pk>/product/', ProductListByCategoryAPIView.as_view(), name="product-detail"),  # /api/category/1/product

    #  Company
    path('company/', CompanyListAPIView.as_view(), name="list"),  # /company/
    path('company/<int:pk>/', CompanyDetailAPIView.as_view(), name="detail"),  # /company/pk
    path('company/<int:pk>/product/', ProductListByCategoryAPIView.as_view(), name="detail"),  # /company/pk/product

    #  Product
]
