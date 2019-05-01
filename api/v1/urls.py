from django.urls import path
from api.v1.views import *


app_name = 'api'

urlpatterns = [
    #  Aktuel
    path('', AktuelListAPIView.as_view(), name="list"),  # /api/aktuel/
    path('<int:pk>/', AktuelDetailAPIView.as_view(), name="detail"),  # /api/aktuel/id/

    #  Category
    path('', CategoryListAPIView.as_view(), name="list"),  # /api/category/
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name="detail"),  # /api/category/1/
    path('<int:pk>/product/', ProductListByCategoryAPIView.as_view(), name="product-detail"),  # /api/category/1/product

    #  Company
    path('', CompanyListAPIView.as_view(), name="list"),  # /company/
    path('<int:pk>/', CompanyDetailAPIView.as_view(), name="detail"),  # /company/pk
    path('<int:pk>/product/', ProductListByCategoryAPIView.as_view(), name="detail"),  # /company/pk/product

    #  Product
]
