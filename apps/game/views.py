from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from apps.users.models import Users
from .forms import GameForm, AttackForm, RevengeForm
import random as rd


# Create your views here.
def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num


def attack(req):
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


# Create your views here.
def findWinner(game, user):
    user_winner = 1  # 0은 패배, 1은 비김, 2는 승리
    user_score = 0  # 따거나 잃은 점수
    if game.bigorsmall == True:  # 큰 수가 이김
        if game.attacker_card > game.revenger_card:
            game.attacker.user_score += game.attacker_card
            game.revenger.user_score -= game.revenger_card
            if game.attacker == user:
                user_winner = 2
                user_score += game.attacker_card
            else:
                user_winner = 0
                user_score -= game.revenger_card
        elif game.attacker_card < game.revenger_card:
            game.attacker.user_score -= game.attacker_card
            game.revenger.user_score += game.revenger_card
            if game.attacker == user:
                user_winner = 0
                user_score -= game.attacker_card
            else:
                user_winner = 2
                user_score += game.revenger_card
    else:
        if game.attacker_card > game.revenger_card:
            game.attacker.user_score -= game.attacker_card
            game.revenger.user_score += game.revenger_card
            if game.attacker == user:
                user_winner = 0
                user_score -= game.attacker_card
            else:
                user_winner = 2
                user_score += game.revenger_card
        elif game.attacker_card < game.revenger_card:
            game.attacker.user_score += game.attacker_card
            game.revenger.user_score -= game.revenger_card
            if game.attacker == user:
                user_winner = 2
                user_score += game.attacker_card
            else:
                user_winner = 0
                user_score -= game.revenger_card
    game.attacker.save()
    game.revenger.save()
    return user_winner, user_score


def revenge(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == "POST":
        form = RevengeForm(request.POST, user=request.user)
        if form.is_valid():
            revenge = form.save(commit=False)
            revenge.revenger = request.user
            revenge.save()

            user_result, user_score = findWinner(revenge, request)
            ctx = {
                "game": revenge,
                "user_result": user_result,
                "user_score": user_score,
            }
            return render(request, "game/detail_result.html", ctx)
    else:
        form = RevengeForm(user=request.user)
        ctx = {"form": form, "pk": pk}
        return render(request, "game/revenge.html", ctx)

    ctx = {"form": form, "pk": pk}
    return render(request, "game/revenge.html", ctx)


def detail_revenge(req, pk):
    game = Game.objects.get(id=pk)
    ctx = {"game": game}
    return render(req, "game/detail_revenge.html", ctx)

def detail_result(req, pk):
    game = Game.objects.get(id=pk)
    user_winner, user_score = findWinner(game,req.user)
    ctx = {'game':game, 'user_winner': user_winner, 'user_score': user_score}
    return render(req, 'game/detail_result.html', ctx)