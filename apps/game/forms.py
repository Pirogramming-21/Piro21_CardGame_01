from django import forms
from .models import Game
import random as rd
from apps.users.models import Users


def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class AttackForm(forms.ModelForm):
    card = forms.ChoiceField(
        choices=[(card, card) for card in shuffle_card()],
        widget=forms.RadioSelect,
        label="Attack Card",
    )

    class Meta:
        model = Game
        fields = [
            "bigorsmall",
            "attacker_card",
            "revenger",
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)  # kwargs dict에서 key가 user인 값 꺼내기
        super().__init__(*args, **kwargs)
        self.fields["bigorsmall"].widget = forms.HiddenInput()
        self.fields["attacker_card"].widget = forms.HiddenInput()
        self.fields["revenger"] = forms.ModelChoiceField(
            queryset=Users.objects.exclude(pk=self.user.pk),
            widget=forms.RadioSelect,
            empty_label=None,
        )

    # AttackForm에서 필요한 것: 공격자의 카드, 공격 대상, 게임 종류?


class RevengeForm(forms.ModelForm):
    card = forms.ChoiceField(
        choices=[(card, card) for card in shuffle_card()],
        widget=forms.RadioSelect,
        label="Revenge Card",
    )

    class Meta:
        model = Game
        fields = ["revenger_card"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields["revenger_card"].widget = forms.HiddenInput()