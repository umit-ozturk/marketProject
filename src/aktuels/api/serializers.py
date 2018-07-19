from rest_framework import serializers

from aktuels.models import AktuelProducts, Aktuel

# CompanyDisplaySerializers

class AktuelModelSerializer(serializers.ModelSerializer):
	aktuel_detail = serializers.SerializerMethodField('get_aktuel_detail_url')

	def get_aktuel_detail_url(self, obj):
		return self.context['request'].build_absolute_uri(obj.slug)

	class Meta:
		model = Aktuel
		fields = [
			'id',
			'title',
			'explain',
			'image_aktuel',
			'slug',
			'aktuel_detail',
			'aktuel_company_name',
			'aktuel_company_site',
			'image_comp'
		]



class AktuelModelDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = AktuelProducts
		fields = [
			'aktuel',
			'name',
			'price',
			'title',
			'exist',
			'updated',
			'image_prod'
		]