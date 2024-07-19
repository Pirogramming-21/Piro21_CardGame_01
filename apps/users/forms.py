from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Users
from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["username", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Users.objects.filter(user_name=username).exists():
            raise ValidationError("This username is already taken.")
        return username