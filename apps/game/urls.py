from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
    path('history/', history, name='history'),
    #path('attack/', attack, name='attack'), # 공격 용
    #path('detail/<int:pk>/', detail, name='detail'), #게임 결과용
    path('ranking/', ranking, name='ranking'),
    path('progressing_result/<int:pk>', progressing_result, name='progressing_result'), #진행 중 용
    path('delete/<int:pk>', game_delete, name='game_delete'), #게임 취소용
    path('revenge/<int:pk>', revenge, name='revenge'),
    path('detail_revenge/<int:pk>', detail_revenge, name='detail_revenge'),
]