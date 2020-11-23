from django.contrib.auth.models import User
from django.db import models
from HOME.models import Mobile
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'User Profile'


class QuestionAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Mobile, related_name='questions', on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True)
    question = models.TextField(null=True)
    answer = models.TextField(null=True)

    def __str__(self):
        return str(self.phone_id)

    class Meta:
        verbose_name = 'Question and Answer'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    review = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'User Reviews'
