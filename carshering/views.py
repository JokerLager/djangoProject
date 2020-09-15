from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListCreateAPIView, get_object_or_404, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response

from carshering.models import Sharing,Image
from carshering.serializers import SharingSerializer, SharingImagesSerializer


class SharingView(ListCreateAPIView):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializer


class SingleSharingView(RetrieveUpdateDestroyAPIView):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializer

class SharingImageView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = SharingImagesSerializer

