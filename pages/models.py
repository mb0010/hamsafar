from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')



class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    date = models.DateTimeField()
    seats_available = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.start_location} to {self.end_location}"


class CompanionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companion_requests')
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
