from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("username",)
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Pick a username",})
        }


class SearchForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("username",)
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username to Search",})
        }

