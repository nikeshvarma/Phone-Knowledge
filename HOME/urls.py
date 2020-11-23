from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('<int:pk>/', views.post_page, name='details_page'),
    path('news/<str:pk>/', views.news_page, name='news_page'),
    path('search/', views.search, name='search'),
    path('searchPhone/', views.search),
    path('compare/', views.compare, name='compare'),
    path('comparision/', views.comparison, name='comparison'),
    path('filter-phones/', views.filter_homepage, name='filter_homepage'),
    path('filter_phones/', views.complete_filter, name='main_filter')
]
