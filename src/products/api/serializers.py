from rest_framework import serializers
from products.models import Product, ProductInfo
from companies.api.serializers import CompanyDisplaySerializer, BrandDisplaySerializer, ProductInfoModelSerializer
from categories.api.serializers import ProductCategoryModelSerializer


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
            'content'
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