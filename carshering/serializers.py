from rest_framework import serializers

from carshering.models import Sharing, Image


class SharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sharing
        fields = ('id', 'name', 'places', 'latitude', 'longitude', 'safetystar',  'images')

class SharingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','image')