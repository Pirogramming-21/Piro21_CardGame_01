from django.contrib import admin
from .models import Game

import apps.game

# Register your models here.

admin.site.register(Game)