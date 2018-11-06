from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from companies.api.serializers import CompanyDisplaySerializer, ProductInfoModelSerializer
from categories.models import Category
from products.models import Product
from versatileimagefield.serializers import VersatileImageFieldSerializer


# -- For Category endpoint --> /api/category/

class CategoryModelSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())
    image_prod = VersatileImageFieldSerializer(sizes='image_prod_first')

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'category_slug',
            'category_defination',
            'category_logo',
            'image_prod',
            'children',
        ]

# -- For Category endpoint --> /api/category/1/product


class ProductByCategoryModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()
    category = CategoryModelSerializer()
    slug = ProductInfoModelSerializer()

    class Meta:
        model = Product
        fields = [
            'category',
            'id',
            'name',
            'price',
            'title',
            'slug',
            'company'
        ]

# -- For Product endpoint --> /api/product/


class ParentCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'category_slug',
            'category_defination',
            'category_logo',
            'parent'
        ]


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    parent = ParentCategoryModelSerializer()
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'category_slug',
            'category_defination',
            'category_logo',
            'parent',
            'children'
        ]
