from django.contrib import admin
from .models import Profile, Review, QuestionAnswers


@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    pass


@admin.register(Review)
class UserReview(admin.ModelAdmin):
    pass


@admin.register(QuestionAnswers)
class QuestionAndAnswer(admin.ModelAdmin):
    pass
