from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=False)
    birth_date = models.DateField(blank=True, null=True)
    signup_date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username
