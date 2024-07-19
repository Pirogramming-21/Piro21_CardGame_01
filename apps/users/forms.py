from django.contrib.auth.forms import UserCreationForm
from .models import Users

class SignupForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username','password1', 'password2']