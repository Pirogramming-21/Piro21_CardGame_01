from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Users(AbstractUser):
    first_name = None
    last_name = None
    user_name = models.CharField(max_length=10, unique=True)
    user_score = models.IntegerField(default=0)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # 기본 'user_set'과 충돌 방지
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # 기본 'user_set'과 충돌 방지
        blank=True,
    )


def __str__(self):
    return self.username
