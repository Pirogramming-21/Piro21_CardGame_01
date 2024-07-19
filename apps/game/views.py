from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from apps.users.models import Users
from .forms import GameForm, AttackForm, RevengeForm
import random as rd
from django.db.models import Q


# Create your views here.
def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num


def attack(request):
    if request.method == "POST":
        game = Game()
        form = AttackForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            if game.revenger != None and game.revenger != request.user:
                game.attacker = request.user
                game.bigorsmall = rd.randint(0, 1)
                game.save()
                return redirect("game:detail_attack", pk=game.pk)
    else:
        game = Game()
        form = AttackForm(request=request, instance=game)
    return render(request, "game/attack.html", {"form": form})


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


from django.db.models import Q


def history(request):
    player = request.user  # 요청으로 들어온 (=현재 로그인 플레이어) 플레이어를 받아옴
    games = Game.objects.filter(Q(attacker=player) | Q(revenger=player)).order_by(
        "-created_date"
    )
    # 공격자 또는 수비자 둘 중 하나라도 플레이어와 일치하는 모든 결과 기록들을 내림차순으로 가져옴
    list = {"games": games}
    return render(request, "game/history.html", list)


def ranking(request):
    user_list = Users.objects.order_by("-user_score")
    if len(user_list) >= 3:
        user_list = user_list[:3]
    return render(request, "game/game_ranking.html", {"user_list": user_list})


def game_delete(request, pk):
    if request.method == "POST":
        Game.objects.get(id=pk).delete()
    return redirect("game:game_list")


def progressing_result(request, pk):
    game = get_object_or_404(Game, pk=pk)
    attacker = game.attacker
    revenger = game.revenger

    data = {"game": game, "attacker": attacker, "revenger": revenger}
    return render(request, "game/progressing_result.html", data)
