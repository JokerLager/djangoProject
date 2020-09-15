from django.urls import path
from .views import ParkingView, SingleParkingView, ParkingImageView

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('parkings/', ParkingView.as_view()),
    path('parkings/<int:pk>', SingleParkingView.as_view()),
    path('parking_images/',ParkingImageView.as_view())
]