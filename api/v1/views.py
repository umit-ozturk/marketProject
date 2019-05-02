from django.db.models import Q
from rest_framework import generics
from aktuels.models import Aktuel, AktuelProducts
from aktuels.serializers import AktuelModelSerializer, AktuelProductModelSerializer
from categories.serializers import CategoryModelSerializer, ProductByCategoryModelSerializer
from categories.models import Category
from companies.models import Company
from companies.serializers import CompanyDisplaySerializer, ProductByCompanyModelSerializer
from products.models import Product


class AktuelListAPIView(generics.ListAPIView):
    queryset = Aktuel.objects.all()
    serializer_class = AktuelModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Aktuel.objects.all()
        return qs


class AktuelDetailAPIView(generics.ListAPIView):
    serializer_class = AktuelProductModelSerializer

    def get_queryset(self, *args, **kwargs):
        aktuel_id = self.kwargs.get("pk")
        qs = AktuelProducts.objects.filter(aktuel_id=aktuel_id)
        return qs


class ProductListByCategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductByCategoryModelSerializer

    def get_queryset(self, *args, **kwargs):
        category_id = self.kwargs.get("pk")
        qs = Product.objects.filter(category=category_id)
        query = self.request.GET.get("q")
        if query:
            query_arg = query.split("-")
            qs = qs.filter(Q(price__range=(query_arg[0], query_arg[1]))).distinct()
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


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDisplaySerializer

    def get_queryset(self, *args, **kwargs):
        qs = Company.objects.filter(level=0)
        return qs


class CompanyDetailAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDisplaySerializer

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        qs = Company.objects.filter(pk=category_id)
        if qs.exists() and qs.count() == 1:
            return qs
        return None


#  Product Apis
