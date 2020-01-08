from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Follow_List


@receiver(post_save, sender=User)
def create_follow_list(sender, instance, created, **kwargs):
    if created:
        Follow_List.objects.create(geek=instance)


@receiver(post_save, sender=User)
def save_follow_list(sender, instance, **kwargs):
    instance.geek.save()
