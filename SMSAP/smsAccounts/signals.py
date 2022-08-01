from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount
from djoser.signals import user_activated
from .models import Profile


@receiver(post_save, sender=UserAccount)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
  
@receiver(post_save, sender=UserAccount)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()

# @receiver(user_activated)
# def activate_profile(user, request, **kwargs):
#     Profile.objects.create(user=user) 