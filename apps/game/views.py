from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Game
from users.models import Users

# Create your views here.
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

