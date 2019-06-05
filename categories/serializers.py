from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from companies.serializers import CompanyDisplaySerializer
from categories.models import Category
from products.models import Product
from versatileimagefield.serializers import VersatileImageFieldSerializer


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


class ProductByCategoryModelSerializer(serializers.ModelSerializer):
    company = CompanyDisplaySerializer()
    category = CategoryModelSerializer()

    class Meta:
        model = Product
        fields = [
            'category',
            'id',
            'name',
            'price',
            'title',
            'company'
        ]


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
