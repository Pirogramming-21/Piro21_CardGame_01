from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Users(AbstractUser):
    first_name = None
    last_name = None
<<<<<<< HEAD
    user_name = models.CharField(max_length=10)
=======
    user_name = models.CharField(max_length=10, null=True)
>>>>>>> 966c6d98fb79ce21f3bfb2deca4e14a8845b038e
    user_score = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_users_groups",  # 고유한 이름으로 변경
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_users_permissions",  # 고유한 이름으로 변경
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    def __str__(self):
        return self.username
