# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    ROLE_STATUS_CHOICES = (
        ("author", "Author"),
        ("guest", "Guest"),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=ROLE_STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username