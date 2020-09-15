from django.contrib import admin

from carshering.models import Sharing, Star, Image


class ParkingAdmin(admin.ModelAdmin):
    list_display =("id","name")

admin.site.register(Sharing)
admin.site.register(Star)
admin.site.register(Image)

# Register your models here.
