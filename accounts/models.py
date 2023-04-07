from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(null=True, blank=True,max_length=140)
