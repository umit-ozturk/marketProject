from companies.models import Company
from companies.api.serializers import CompanyDisplaySerializer, ProductByCompanyModelSerializer
from products.models import Product
from django.db.models import Q
from rest_framework import generics


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


class ProductListByCategoryAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = ProductByCompanyModelSerializer

    def get_queryset(self, *args, **kwargs):
        company_id = self.kwargs.get("pk")
        qs = Product.objects.filter(company=company_id)
        query = self.request.GET.get("q")
        if query:
            query_arg = query.split("-")
            qs = qs.filter(
                Q(price__range=(query_arg[0], query_arg[1]))
                ).distinct()
        return qs
