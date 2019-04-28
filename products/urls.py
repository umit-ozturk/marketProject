from django.urls import path

from .views import(
    ProductDetailView,
    )


app_name = 'products'

urlpatterns = [

    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),  # /product/1/
]