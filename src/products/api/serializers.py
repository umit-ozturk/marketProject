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
			'exist',
			'image_prod',
			'company',
			'category'
		]

class ProductFeaturedModelSerializer(serializers.ModelSerializer):
	company = CompanyDisplaySerializer()
	
	class Meta:
		model = Product
		fields = [
			'id',
			'name',
			'price',			
			'image_prod',
			'company'
		]