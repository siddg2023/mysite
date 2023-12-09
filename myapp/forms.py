# forms.py
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'major_area_of_study', 'year_in_program', 'bio']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RecruiterProfile

class RecruiterSignupForm(UserCreationForm):
    company = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User  # Use the User model, not RecruiterProfile
        fields = ['username', 'password1', 'password2']

