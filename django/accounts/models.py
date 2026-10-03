import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """One account shared by customer and staff experiences."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=150, blank=True)


class AuthIdentity(models.Model):
    class Provider(models.TextChoices):
        GOOGLE = 'google', 'Google'
        APPLE = 'apple', 'Apple'
        FACEBOOK = 'facebook', 'Facebook'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auth_identities')
    provider = models.CharField(max_length=16, choices=Provider.choices)
    provider_subject = models.CharField(max_length=255)
    linked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['provider', 'provider_subject'],
                name='unique_auth_provider_subject',
            ),
        ]
