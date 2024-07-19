from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Game(models.Model):
    bigorsmall = models.BooleanField()

    attacker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="attack_game",
    )
    attacker_card = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    revenger = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="revenge_game",
    )
    revenger_card = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], null=True, blank=True
    )

    created_date = models.DateTimeField(default=timezone.now)
