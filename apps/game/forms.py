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

    class Meta:
        model = Game
        fields = [
            "attacker_card",
            "revenger",
        ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AttackForm, self).__init__(*args, **kwargs)
        self.shuffleChoices()

    def shuffleChoices(self):
        if self.request:
            random_numbers = shuffle_card()
            choices = [(str(num), str(num)) for num in random_numbers]
            self.fields["attacker_card"] = forms.ChoiceField(
                choices=choices, widget=forms.RadioSelect, label="Attacker Card"
            )

    revenger = forms.ModelChoiceField(queryset=Users.objects.all(), label="Revenger")



class RevengeForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["revenger_card"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RevengeForm, self).__init__(*args, **kwargs)
        self.shuffleChoices()
    
    def shuffleChoices(self):
        if self.request:
            random_numbers = shuffle_card()
            choices = [(str(num), str(num)) for num in random_numbers]
            self.fields['revenger_card'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect,  label="Revenger Card")