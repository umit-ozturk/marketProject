from rest_framework.views import APIView
from rest_framework import generics
from django.db.models import Q
from products.models import Product




from .pagination import (
	StandartResultsPagination,
	FeaturedResultsPagination
	)
from .serializers import (
	ProductModelSerializer,
	ProductFeaturedModelSerializer,
	ProductCategoriesModelSerializer
	)



class ProductDetailAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductModelSerializer

	def get_queryset(self, *args, **kwargs):
		product_id = self.kwargs.get("pk")
		qs = Product.objects.filter(pk=product_id)
		if qs.exists() and qs.count() == 1:
			return qs
		return None

class ProductListAPIView(generics.ListAPIView):
	serializer_class = ProductModelSerializer
	pagination_class = StandartResultsPagination

	def get_queryset(self, *args, **kwargs):
		qs = Product.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(name__icontains=query) |
				Q(price__icontains=query) |
				Q(title__icontains=query)
				)
		return qs

class ProductFeaturedListAPIView(generics.ListAPIView):
	serializer_class = ProductFeaturedModelSerializer
	pagination_class = FeaturedResultsPagination

	def get_queryset(self, *args, **kwargs):
		qs = Product.objects.all()
		return qs


class ProductCategoriesListAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductCategoriesModelSerializer
	pagination_class = StandartResultsPagination

	def get_queryset(self, *args, **kwargs):
		produc_category_id = self.kwargs.get("pk")
		print(produc_category_id)
		qs = Product.objects.all()
		return qs










