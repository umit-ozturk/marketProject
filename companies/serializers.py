from rest_framework import serializers
from companies.models import Company, Brand
from products.models import Product, ProductInfo
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_recursive.fields import RecursiveField


class ProductInfoModelSerializer(serializers.ModelSerializer):
    image_prod_first = VersatileImageFieldSerializer(sizes='image_prod_first')
    image_prod_second = VersatileImageFieldSerializer(sizes='image_prod_second')
    image_prod_third = VersatileImageFieldSerializer(sizes='image_prod_third')
    image_prod_fourth = VersatileImageFieldSerializer(sizes='image_prod_fourth')

    class Meta:
        model = ProductInfo
        fields = [
            'id',
            'slug',
            'image_prod_first',
            'image_prod_second',
            'image_prod_third',
            'image_prod_fourth',
            'get_slug_count',
            'created_at',
            'updated_at'
        ]


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
    slug = ProductInfoModelSerializer()
    company = CompanyDisplaySerializer()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'title',
            'slug',
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


class ProductInfoModelSerializer(serializers.ModelSerializer):
    image_prod_first = VersatileImageFieldSerializer(sizes='image_prod_first')
    image_prod_second = VersatileImageFieldSerializer(sizes='image_prod_second')
    image_prod_third = VersatileImageFieldSerializer(sizes='image_prod_third')
    image_prod_fourth = VersatileImageFieldSerializer(sizes='image_prod_fourth')

    class Meta:
        model = ProductInfo
        fields = [
            'id',
            'slug',
            'image_prod_first',
            'image_prod_second',
            'image_prod_third',
            'image_prod_fourth',
            'get_slug_count',
            'created_at',
            'updated_at'
        ]
