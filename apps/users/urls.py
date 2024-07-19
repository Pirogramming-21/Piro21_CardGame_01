from django.urls import path, include
from .views import *

app_name = "users"

urlpatterns = [
    path("", main, name="main"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),
]
