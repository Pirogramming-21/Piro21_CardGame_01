from django import forms
from .models import Game
import random as rd
from users.models import User


def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class AttackForm(forms.ModelForm):
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
        self.fields["revenger"].queryset = User.objects.exclude(pk=self.user.pk)
        self.fields["revenger"].label = "Choose who to attack"
        cards = shuffle_card()
        choices = [("---------", "---------")] + [(card, str(card)) for card in cards]
        self.fields["attacker_card"].choices = choices

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.attacker = self.user
        instance.attacker_card = self.cleaned_data["attacker_card"]
        if commit:
            instance.save()
        return instance

    # AttackForm에서 필요한 것: 공격자의 카드, 공격 대상, 게임 종류?
