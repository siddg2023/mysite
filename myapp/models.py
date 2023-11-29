from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, default='None')
    last_name = models.CharField(max_length=100, default='None')
    email = models.EmailField(default='test@gmail.com')
    phone_number = models.CharField(max_length=15, default='None')
    major_area_of_study = models.CharField(max_length=100, default='None')
    year_in_program = models.PositiveIntegerField(default=1)
    bio = models.TextField(default='None')

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Profile"

