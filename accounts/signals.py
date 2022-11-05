from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.models import User, UserProfile



@receiver(post_save, sender=User)
def create_profile_receiver(sender, instance, created, **kwargs):
    """
    This is receiver function to automatically create a user profile
    once user is created or update the existing user profile
    """
    if created:
        create_profile = UserProfile.objects.create(
            user = instance
        )
        create_profile.save()
       
    elif not created:
        try:
            user_profile = UserProfile.objects.get_or_create(
                user = instance
            )
            user_profile.save()
        except:
            pass