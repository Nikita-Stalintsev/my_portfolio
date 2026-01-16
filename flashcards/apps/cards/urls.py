from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('deck/add/', DeckCreateView.as_view(), name='deck_add'),
    path("deck/delete/", DeckDeleteView.as_view(), name="deck_delete"),
    path('deck/<slug:slug>/add/', CardCreateView.as_view(), name='card_add'),
    path('deck/<slug:slug>/card/', CardView.as_view(), name="card"),
    path('deck/<slug:slug>/', DeckView.as_view(), name="deck"),
    path('deck/<slug:slug>/cards/delete/', CardDeleteView.as_view(), name='card_delete'),

]
