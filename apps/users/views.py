from django.shortcuts import render, redirect
from apps.users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Users
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def main(req):
    return render(req, "users/main.html")


def signup(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if Users.objects.filter(username=username).exists():
                messages.error(req, "Username already exists")
                return render(req, "users/signup.html", {"form": form})
            user = form.save()
            # auth_login(req, user)
            return redirect("users:main")
        else:
            return render(req, "users/signup.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(req, "users/signup.html", {"form": form})


def login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(req, user)
            return redirect("users:main")
        else:
            context = {
                "form": form,
            }
            return render(req, template_name="users/login.html", context=context)
    else:
        form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(req, template_name="users/login.html", context=context)


def logout(req):
    auth.logout(req)
    return redirect("users:main")
