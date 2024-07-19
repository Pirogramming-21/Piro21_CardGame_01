from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('history/', history, name='history'),
    #path('attack/', attack, name='attack'), # 공격 용
    #path('counter/<int:pk>', counter, name='counter'), #카운터어택 디테일용
    #path('detail/<int:pk>/', detail, name='detail'), #게임 결과용
    path('ranking/', ranking, name='ranking'),
    path('progressing_result/<int:pk>', progressing_result, name='progressing_result'), #진행 중 용
    #path('detail_defend/<int:pk>', detail_defend, name='detail_defend'), #방어 디테일용
    path('delete/<int:pk>', game_delete, name='game_delete') #게임 취소용
]