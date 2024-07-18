from django.urls import path
from django.shortcuts import render, redirect
from .models import Game
from .views import *

app_name = "game"

urlpatterns = [
    path("attack/<int:pk>", attack, name="attack"),
    path("detail_attack/<int:pk>", detail_attack, name="detail_attack"),
]
