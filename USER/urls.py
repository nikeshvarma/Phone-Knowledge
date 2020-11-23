from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.updateprofile, name='updateprofile'),
    path('<str:pk>/add-review/', views.review, name='review'),
    path('<str:pk>/add-question/', views.question_answer, name='question')
]
