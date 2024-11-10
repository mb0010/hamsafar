from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Trip, CompanionRequest


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'age', 'location', 'phone_number', 'password1', 'password2']


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_location', 'end_location', 'date', 'seats_available', 'description']


class CompanionRequestForm(forms.ModelForm):
    class Meta:
        model = CompanionRequest
        fields = ['start_location', 'end_location', 'date', 'description']
