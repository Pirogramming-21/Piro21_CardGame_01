from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
#   path('', main, name='main'),  예시임
    path("attack/", attack, name="attack"),
    path("detail_attack/<int:pk>", detail_attack, name="detail_attack"),
    path('revenge/<int:pk>', revenge, name='revenge'),
    path('detail_revenge/<int:pk>', detail_revenge, name='detail_revenge')
]