from django.urls import path
from . import views

urlpatterns = [
    path('filter-brands/brand-search/', views.brand_search, name='brandsearch')
]