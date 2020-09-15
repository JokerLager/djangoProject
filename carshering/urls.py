from django.urls import path

from carshering.views import SharingView, SingleSharingView, SharingImageView

app_name = "samocatsharing"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('sharings/', SharingView.as_view()),
    path('parkings/<int:pk>', SingleSharingView.as_view()),
    path('parking_images/',SharingImageView.as_view()),
]