from rest_framework import serializers
from products.models import Product
from companies.serializers import CompanyDisplaySerializer, BrandDisplaySerializer
from categories.serializers import ProductCategoryModelSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()
    category = ProductCategoryModelSerializer()
    brand = BrandDisplaySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'old_price',
            'price',
            'title',
            'get_sale_percent',
            'company',
            'category',
            'brand',
            'content',
            'feature'
        ]


class ProductFeaturedModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'company'
         ]


class ProductCategoriesModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'company'
        ]
