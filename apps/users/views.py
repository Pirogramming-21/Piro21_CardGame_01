from django.shortcuts import render, redirect
from apps.users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Users
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError

# Create your views here.


def main(req):
    return render(req, "users/main.html")


def signup(req):
    if req.method == "GET":
        form = SignupForm(req.POST)
        ctx = {"form": form}
        return render(req, "users/signup.html", ctx)

    form = SignupForm(req.POST)
    if form.is_valid():
        form.save()
    ctx = {"form": form}
    return redirect("users:main")


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
