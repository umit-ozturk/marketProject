from django.urls import path

from .views import(
    ProductDetailView,
    SearchView
    )


app_name = 'products'

urlpatterns = [
    path('search', SearchView.as_view(), name="search-list"),  # /product/
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),  # /product/1/
]