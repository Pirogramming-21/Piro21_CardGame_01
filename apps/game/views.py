from .models import Game
from apps.users.models import Users
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

# Create your views here.
def findWinner(game, user):
    user_winner = 1 # 0은 패배, 1은 비김, 2는 승리
    user_score = 0  # 따거나 잃은 점수
    if game.bigorsmall == True: # 큰 수가 이김
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

def revenge(req, pk):
    game = Game.objects.get(id=pk)
    if req.method == "GET":
        form = revengeForm(request = req, instance = game)
        ctx = {'form': form, 'pk':pk}
        return render(req, 'game/revenge.html', ctx)
    
    form = revengeForm(req.POST, instance = game)
    if form.is_valid():
            game = form.save()
            user_result, user_score = findWinner(game, req)
            ctx = {'game': game, 'user_result':user_result, 'user_score':user_score}
    return render(req, 'game/detail_result.html', ctx)

def detail_revenge(req, pk):
    game = Game.objects.get(id=pk)
    ctx = {'game': game}
    return render(req, 'game/detail_revenge.html', ctx)
from django.db.models import Q

def history(request):     
    player = request.user # 요청으로 들어온 (=현재 로그인 플레이어) 플레이어를 받아옴     
    games = Game.objects.filter(Q(attacker = player) | Q(revenger=player)).order_by('-created_date')     
    # 공격자 또는 수비자 둘 중 하나라도 플레이어와 일치하는 모든 결과 기록들을 내림차순으로 가져옴     
    list = {'games':games}     
    return render(request, 'game/history.html', list)

def ranking(request):
    user_list = Users.objects.order_by('-user_score')
    if len(user_list) >= 3:
        user_list = user_list[:3]
    return render(request, 'game/game_ranking.html', {'user_list':user_list})

def game_delete(request, pk):
    if request.method == 'POST':
        Game.objects.get(id=pk).delete()
    return redirect('game:game_list')

def progressing_result(request, pk):
    game = get_object_or_404(Game, pk=pk)
    attacker = game.attacker
    revenger = game.revenger

    data = {'game':game, 'attacker':attacker, 'revenger':revenger}
    return render(request, 'game/progressing_result.html', data)

