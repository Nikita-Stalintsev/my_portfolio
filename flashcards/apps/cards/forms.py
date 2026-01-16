from django import forms
from .models import *


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ('title', 'category', 'description',)


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ('name', 'content')


class DeckDeleteForm(forms.Form):
    deck = forms.ModelChoiceField(
        queryset=Deck.objects.order_by("title"),
        empty_label="— выбери колоду —",
        label="Колода",
        widget=forms.Select(attrs={"class": "form-control"})
    )


class CardDeleteForm(forms.Form):
    card = forms.ModelChoiceField(
        queryset=Card.objects.none(),
        empty_label="— выбери карточку —",
        label="Карточка",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    def __init__(self, *args, deck=None, **kwargs):
        super().__init__(*args, **kwargs)
        if deck is not None:
            self.fields["card"].queryset = Card.objects.filter(deck=deck).order_by("name")
