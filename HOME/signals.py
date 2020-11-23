from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mobile, Price, MobilePictures


@receiver(post_save, sender=Mobile)
def create_image_field(sender, instance, created, **kwargs):
    print(instance)
    if created:
        MobilePictures.objects.create(phone=instance)


@receiver(post_save, sender=Mobile)
def create_price_field(sender, instance, created, **kwargs):
    if created:
        Price.objects.create(phone=instance)
