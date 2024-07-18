from django.shortcuts import render, redirect
from .models import Game
from users.models import User
from .forms import GameForm, AttackForm


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


def attack(req, pk):
    game = Game.objects.get(id=pk)
    if req.method == "GET":
        form = GameForm(request=req, instance=game)
        ctx = {"form": form, "pk": pk}
        return render(req, "game/revenge.html", ctx)

    form = GameForm(req.POST, instance=game)
    if form.is_valid():
        game = form.save()
        user_result, user_score = findWinner(game, req)
        ctx = {"game": game, "user_result": user_result, "user_score": user_score}
    return render(req, "game/detail_result.html", ctx)


def detail_attack(req, pk):
    game = Game.objects.get(id=pk)
    ctx = {"game": game}
    return render(req, "game/detail_attack.html", ctx)
