from django import forms
from .models import Game, Users
from django.core.validators import MaxValueValidator, MinValueValidator
import random as rd

def shuffle_card():
    rd_num = sorted(rd.sample(range(1, 11), 5))
    return rd_num

class revengeForm(forms.ModelForm):
    class Meta:
        model=Game
        fields = ['revenger_card']
    
    # args, kwargs는 각각 request와 instance
    def __init__(self, *args, **kwargs):
        super(revengeForm,self).__init__(*args,**kwargs)