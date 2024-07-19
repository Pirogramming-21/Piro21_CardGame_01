from django.urls import path
from django.shortcuts import render, redirect
from .models import Game
from .views import *

app_name = "game"

urlpatterns = [
    path("attack/", attack, name="attack"),
    path("detail_attack/<int:pk>", detail_attack, name="detail_attack"),
    path("revenge/<int:pk>", revenge, name="revenge"),
    path("detail_revenge/<int:pk>", detail_revenge, name="detail_revenge"),
    path("history/", history, name="history"),
    # path('detail/<int:pk>/', detail, name='detail'), #게임 결과용
    path("ranking/", ranking, name="ranking"),
    path(
        "progressing_result/<int:pk>", progressing_result, name="progressing_result"
    ),  # 진행 중 용
    path("delete/<int:pk>", game_delete, name="game_delete"),  # 게임 취소용
    path("detail_revenge/<int:pk>", detail_revenge, name="detail_revenge"),
]
