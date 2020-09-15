from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListCreateAPIView, get_object_or_404, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from parking.models import Parking, Image
from parking.serializers import ParkingSerializer, ParkingImagesSerializer


class ParkingView(ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


class SingleParkingView(RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

class ParkingImageView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ParkingImagesSerializer

