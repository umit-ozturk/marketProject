from rest_framework import serializers
from accounts.models import UserProfile
from versatileimagefield.serializers import VersatileImageFieldSerializer


class UserProfileModelSerializer(serializers.ModelSerializer):
    userphoto = VersatileImageFieldSerializer(sizes='userphoto')

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'name',
            'surname',
            'birthday',
            'gender',
            'phone',
            'userphoto'
        ]
