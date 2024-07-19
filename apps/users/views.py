from django.shortcuts import render, redirect
from apps.users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Users
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.core.exceptions import ValidationError


# Create your views here.


def main(req):
    return render(req, "users/main.html")


def signup(req):
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            try:
                user = form.save()
                auth_login(req, user)
                messages.success(req, "회원가입에 성공했습니다.")
                return redirect("users:main")
            except ValidationError as e:
                # 유효성 검사에서 오류가 발생한 경우
                form.add_error(None, e)
                messages.error(req, "회원가입 중 오류가 발생했습니다.")
                return render(req, "users/signup.html", {"form": form})
        else:
            messages.error(req, "폼에 오류가 있습니다.")
            return render(req, "users/signup.html", {"form": form})
    else:
        form = SignupForm()
        return render(req, "users/signup.html", {"form": form})


def login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(req, user)
            messages.success(req, "로그인에 성공했습니다.")
            return redirect("users:main")  # 로그인 후 이동할 페이지 URL 이름
        else:
            messages.error(
                req, "로그인에 실패했습니다. 사용자 이름 또는 비밀번호를 확인하세요."
            )
            return render(req, "users/login.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(req, "users/login.html", {"form": form})


def logout(req):
    auth.logout(req)

    return redirect("users:main")

