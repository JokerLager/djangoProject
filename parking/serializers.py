from rest_framework import serializers

from parking.models import Parking, Image


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'name', 'places', 'latitude', 'longitude', 'safetystar', 'comfortstar', 'images')

class ParkingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','image')
