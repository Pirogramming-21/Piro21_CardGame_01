from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Users


class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["username", "password1", "password2"]

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        if Users.objects.filter(user_name=user_name).exists():
            raise ValidationError("This username is already taken.")
        return user_name
