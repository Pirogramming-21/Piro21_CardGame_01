from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["username", "password1", "password2"]
