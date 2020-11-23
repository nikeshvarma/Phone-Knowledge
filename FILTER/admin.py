from django.contrib import admin
from .models import *


@admin.register(Brands)
class Brands(admin.ModelAdmin):
    list_per_page = 20



@admin.register(PriceRange)
class PriceRange(admin.ModelAdmin):
    list_display = ['label']


@admin.register(RAM)
class RAM(admin.ModelAdmin):
    pass
