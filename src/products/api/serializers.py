from rest_framework import serializers

from products.models import Product


from companies.api.serializers import CompanyDisplaySerializer
from categories.api.serializers import ProductCategoryModelSerializer

class ProductModelSerializer(serializers.ModelSerializer):
	company = CompanyDisplaySerializer()
	category = ProductCategoryModelSerializer()
	
	class Meta:
		model = Product
		fields = [
			'id',
			'name',
			'price',
			'title',
			'image_prod_first',
			'image_prod_second',
			'image_prod_third',
			'image_prod_fourth',
			'get_sale_percent',
			'get_slug_count',
			'company',
			'category',
			'content'
		]

class ProductFeaturedModelSerializer(serializers.ModelSerializer):
	company = CompanyDisplaySerializer()
	
	class Meta:
		model = Product
		fields = [
			'id',
			'name',
			'price',			
			'image_prod_first',
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
			'image_prod_first',
			'company'
		]