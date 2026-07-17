from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, default="user")
    status = models.CharField(max_length=20, default="active")

    def __str__(self):
        return self.username