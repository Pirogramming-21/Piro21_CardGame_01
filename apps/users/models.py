from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    first_name = None
    last_name = None
    user_name = models.CharField(max_length=10, unique=True)
    user_score = models.IntegerField(default=0)

    def __str__(self):
        return self.username