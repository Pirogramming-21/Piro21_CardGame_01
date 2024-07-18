from django.urls import path, include
from .views import *

app_name = 'game'

urlpatterns = [
#   path('', main, name='main'),  예시임
    path('revenge/<int:pk>', revenge, name='revenge'),
    path('detail_revenge/<int:pk>', detail_revenge, name='detail_revenge')

]