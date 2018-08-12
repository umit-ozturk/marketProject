from rest_framework import serializers
from companies.models import Company, Brand


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

