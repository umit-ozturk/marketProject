from rest_framework import serializers
from products.models import Product
from companies.serializers import CompanyDisplaySerializer, BrandDisplaySerializer, ProductInfoModelSerializer
from categories.serializers import ProductCategoryModelSerializer


class ProductModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()
    category = ProductCategoryModelSerializer()
    brand = BrandDisplaySerializer()
    slug = ProductInfoModelSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'old_price',
            'price',
            'title',
            'slug',
            'get_sale_percent',
            'company',
            'category',
            'brand',
            'content',
            'feature'
        ]


class ProductFeaturedModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()
    slug = ProductInfoModelSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'slug',
            'company'
         ]


class ProductCategoriesModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()
    slug = ProductInfoModelSerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'slug',
            'company'
        ]
