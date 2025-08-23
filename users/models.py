# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserBase(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
