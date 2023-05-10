from django.db import models
from django.contrib.auth.models import AbstractUser


user_types = (
    ('User', 'User'),
    ('Organization','Organization'),
)

# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(choices=user_types, max_length=15)