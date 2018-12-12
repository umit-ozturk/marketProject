from rest_framework import generics
from django.db.models import Q
from products.models import Product, ProductInfo
from itertools import chain
from .pagination import (
    FeaturedResultsPagination,
    StandartMainPageProductResultsPagination
    )
from .serializers import (
    ProductModelSerializer,
    ProductFeaturedModelSerializer
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
    pagination_class = StandartMainPageProductResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs_id_list = ProductSlugAPIView.product_for_slug_min_price()
        qs = Product.objects.filter(id__in=qs_id_list)
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


class ProductSlugAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        qs = [Product.objects.filter(slug__slug=slug).order_by("price").first()]
        return qs

    @staticmethod
    def product_for_slug_min_price():
        slug_list = ProductInfo.objects.all().values_list('id', flat=True)
        none_qs = Product.objects.none()
        prod_list = []
        for slug in slug_list:
            if Product.objects.filter(slug_id=slug).count() == 1:
                single_prod = Product.objects.filter(slug_id=slug).first()
            if Product.objects.filter(slug_id=slug).count() > 1:
                single_prod = Product.objects.filter(slug_id=slug).order_by("price").first()
            else:
                pass
            #prod_list.append(single_prod.id)
        qs = list(chain(none_qs, prod_list))
        return qs
