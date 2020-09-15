from django.contrib import admin
from .models import Parking,ComfortStar,Image,SafetyStar

class ParkingAdmin(admin.ModelAdmin):
    list_display =("id","name")

admin.site.register(Parking)
admin.site.register(ComfortStar)
admin.site.register(Image)
admin.site.register(SafetyStar)

# Register your models here.
