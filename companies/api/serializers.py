from rest_framework import serializers
from companies.models import Company, Brand
from products.models import ProductInfo
from versatileimagefield.serializers import VersatileImageFieldSerializer


class ParentCompanyDisplaySerializer(serializers.ModelSerializer):

	class Meta:
		model = Company
		fields = [
			'id',
			'company_name',
			'company_site',
			'company_description',
			'image_comp',
			'parent'
		]


class CompanyDisplaySerializer(serializers.ModelSerializer):
	parent = ParentCompanyDisplaySerializer()

	class Meta:
		model = Company
		fields = [
			'id',
			'company_name',
			'company_site',
			'image_comp',
			'company_description',
			'parent'
		]


class BrandDisplaySerializer(serializers.ModelSerializer):
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
			'get_slug_count'
		]