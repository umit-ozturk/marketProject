from django.db.models import Q
from categories.models import Category
from products.models import Product
from rest_framework import generics
from .serializers import (
	CategoryModelSerializer,
	ProductByCategoryModelSerializer
	)


class ProductListByCategoryAPIView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = ProductByCategoryModelSerializer

	def get_queryset(self, *args, **kwargs):
		category_id = self.kwargs.get("pk")
		qs = Product.objects.filter(category=category_id)
		query = self.request.GET.get("q")
		if query:
			query_arg = query.split("-")
			qs = qs.filter(
				Q(price__range=(query_arg[0], query_arg[1]))
				).distinct()	
		return qs


class CategoryDetailAPIView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryModelSerializer

	def get_queryset(self, *args, **kwargs):
		category_id = self.kwargs.get("pk")
		qs = Category.objects.filter(pk=category_id)
		if qs.exists() and qs.count() == 1:
			return qs		
		return None


class CategoryListAPIView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryModelSerializer

	def get_queryset(self, *args, **kwargs):
		qs = Category.objects.filter(level=0)
		return qs