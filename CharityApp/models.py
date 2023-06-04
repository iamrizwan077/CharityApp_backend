from django.db import models
from django.contrib.auth.models import AbstractUser


user_types = (
    ('User', 'User'),
    ('Organization','Organization'),
)

class CustomUser(AbstractUser):
    user_type = models.CharField(choices=user_types, max_length=15)

    def __str__(self) -> str:
        return self.email
    
    def natural_key(self):
        return (self.email,)


class Organization(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    mission = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name
    
    # def natural_key(self):
    #     return (self.name,)


class Donation(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
