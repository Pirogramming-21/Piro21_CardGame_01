from django.db import models
from apps.users.models import Users
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import random as rd


def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num


# Create your models here.
class Game(models.Model):
    bigorsmall = models.BooleanField()

    attacker = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="attack_game",
    )
    attacker_card = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    revenger = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="revenge_game",
    )
    revenger_card = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], null=True, blank=True
    )

    created_date = models.DateTimeField(default=timezone.now)
