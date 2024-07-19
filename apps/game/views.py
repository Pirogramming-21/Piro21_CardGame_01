from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from users.models import User
from .forms import GameForm, AttackForm
import random as rd


# Create your views here.
def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num


def attack(req, pk):
    game = get_object_or_404(Game, pk=pk)

    if req.method == "POST":
        form = AttackForm(req.POST, user=req.user)
        if form.is_valid():
            attack = form.save(commit=False)
            attack.attacker_card = form.cleaned_data["card"]
            attack.save()
            ctx = {"form": form, "attack": attack}
            return render(req, "game/revenge.html", ctx)
        else:
            return render(req, "game/detail_result.html", {"form": form, "game": game})

    else:
        form = AttackForm(user=req.user)
        ctx = {"form": form, "game": game}
        return render(req, "game/detail_result.html", ctx)


def detail_attack(req, pk):
    game = Game.objects.get(pk=pk)
    ctx = {"game": game}
    return render(req, "game/detail_attack.html", ctx)
