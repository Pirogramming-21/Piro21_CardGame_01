from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('',main, name="main"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="singup"),
#   path('/users', login, name='login'), 예시임
]