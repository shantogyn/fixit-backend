from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    
    phone_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, default="customer")
    status = models.CharField(max_length=20, default="active")
    login_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.username