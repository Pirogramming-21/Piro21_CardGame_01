from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    user_score = models.IntegerField(default=0)
    email = None
    nickname = None
    birth = None
    gender = None
    job = None
    desc = None