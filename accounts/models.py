from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def add_to_default_group(sender, instance=None, created=False, **kwargs):
    """
    Add the default group to access the Tourist Spots
    """
    if created:
        group = Group.objects.get(name='Spots')
        instance.groups.add(group)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Create Token when user are created
    """
    if created:
        Token.objects.create(user=instance)
