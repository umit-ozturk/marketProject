from rest_framework import serializers
from companies.models import Company, Brand
from products.models import Product
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_recursive.fields import RecursiveField


class CompanyDisplaySerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())
    image_comp = VersatileImageFieldSerializer(sizes='image_comp')

    class Meta:
        model = Company
        fields = [
            'id',
            'company_name',
            'company_site',
            'image_comp',
            'company_description',
            'created_at',
            'updated_at',
            'children'
        ]


class ProductByCompanyModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'title',
            'company',
            'get_sale_percent'
        ]


class BrandDisplaySerializer(serializers.ModelSerializer):
    brand_image = VersatileImageFieldSerializer(sizes='brand_image')

    class Meta:
        model = Brand
        fields = [
            'id',
            'brand_name',
            'brand_site',
            'brand_description',
            'brand_image',
            'created_at',
            'updated_at'
        ]

