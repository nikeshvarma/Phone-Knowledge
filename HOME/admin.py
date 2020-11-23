from django.contrib import admin
from .models import *


@admin.register(CarouselPhotos)
class CarouselPictures(admin.ModelAdmin):
    pass


@admin.register(Mobile)
class Mobiles(admin.ModelAdmin):
    pass


@admin.register(MobilePictures)
class MobilePictures(admin.ModelAdmin):
    pass


@admin.register(LatestNews)
class LatestNews(admin.ModelAdmin):
    pass


@admin.register(Price)
class PhonePrice(admin.ModelAdmin):
    pass


@admin.register(UpcomingPhones)
class UpcomingPhones(admin.ModelAdmin):
    pass
