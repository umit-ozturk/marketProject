from rest_framework import serializers
from aktuels.models import AktuelProducts, Aktuel, AktuelSlug
from versatileimagefield.serializers import VersatileImageFieldSerializer


class AktuelModelSerializer(serializers.ModelSerializer):
    image_aktuel = VersatileImageFieldSerializer(sizes='image_aktuel')
    image_aktuel_comp = VersatileImageFieldSerializer(sizes='image_aktuel_comp')

    class Meta:
        model = Aktuel
        fields = [
            'id',
            'slug',
            'image_aktuel',
            'image_aktuel_comp'
        ]


class AktuelSlugModelSerializer(serializers.ModelSerializer):
    image_aktuel_prod = VersatileImageFieldSerializer(sizes='image_aktuel_prod')

    class Meta:
        model = AktuelSlug
        fields = [
            'title',
            'explain',
            'aktuel_company_name',
            'aktuel_company_site'
        ]


class AktuelProductModelSerializer(serializers.ModelSerializer):
    image_aktuel_prod = VersatileImageFieldSerializer(sizes='image_aktuel_prod')

    class Meta:
        model = AktuelProducts
        fields = [
            'aktuel',
            'image_aktuel_prod'
        ]
