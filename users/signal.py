from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Acc

@receiver(post_save, sender=User)
def created_acc(sender, instance, created, **kwargs):
    if created:
        Acc.objects.create(user=instance)

