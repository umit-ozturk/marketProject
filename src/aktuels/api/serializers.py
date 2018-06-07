from rest_framework import serializers

from aktuels.models import Aktuel, AktuelProducts

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
			'timestamp',
			'slug',
			'aktuel_detail'
		]



class AktuelModelDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = AktuelProducts
		fields = [
			'id',
			'aktuel',
			'title',
			'price',
			'exist',
			'updated',
			'timestamp',
			'image_prod'

		]