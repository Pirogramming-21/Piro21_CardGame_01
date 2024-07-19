from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup-input'
            }
        )
    )

    email = None
    name = None
    nickname = None
    gender = None
    job = None
    birth = None
    desc = None
    class Meta:
        model = Users
        fields = ['username','password1', 'password2']
    