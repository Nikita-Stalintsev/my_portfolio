import random
from django.db.models import Max
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, TemplateView
from .models import *
from .forms import *


class IndexView(ListView):
    model = Deck
    template_name = "cards/index.html"
    context_object_name = "decks"

    def get_queryset(self):
        return (
            Deck.objects
            .annotate(last_card_update=Max("cards__updated_at"))
            .order_by("title")
        )


class DeckView(ListView):
    model = Card
    template_name = "cards/deck.html"
    context_object_name = "cards"

    def get_queryset(self):
        self.deck = get_object_or_404(Deck, slug=self.kwargs["slug"])
        return Card.objects.filter(deck=self.deck)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["deck"] = self.deck
        return context


class DeckCreateView(CreateView):
    model = Deck
    form_class = DeckForm
    template_name = "cards/add-deck.html"
    success_url = reverse_lazy('index')


class DeckReview(ListView):
    model = Card
    template_name = "cards/card.html"


class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "cards/add-card.html"

    def dispatch(self, request, *args, **kwargs):
        self.deck = get_object_or_404(Deck, slug=self.kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.deck = self.deck
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("deck", kwargs={"slug": self.deck.slug})


class DeckDeleteView(FormView):
    template_name = "cards/delete-deck.html"
    form_class = DeckDeleteForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        deck = form.cleaned_data["deck"]
        deck.delete()
        return super().form_valid(form)


class CardView(TemplateView):
    template_name = "cards/card.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        deck = get_object_or_404(Deck, slug=self.kwargs["slug"])
        qs = Card.objects.filter(deck=deck).order_by("id")

        context["deck"] = deck

        if not qs.exists():
            context["card"] = None
            return context

        current_id = self.request.GET.get("card")
        current = None
        if current_id and current_id.isdigit():
            current = qs.filter(id=int(current_id)).first()

        mode = self.request.GET.get("mode", "start")

        if mode == "random":
            context["card"] = random.choice(list(qs))
            return context

        if current is None:
            context["card"] = qs.first()
            return context

        nxt = qs.filter(id__gt=current.id).first()
        context["card"] = nxt if nxt else qs.first()
        return context


class CardDeleteView(FormView):
    template_name = "cards/delete-card.html"
    form_class = CardDeleteForm

    def dispatch(self, request, *args, **kwargs):
        self.deck = get_object_or_404(Deck, slug=self.kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["deck"] = self.deck
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["deck"] = self.deck
        return context

    def form_valid(self, form):
        card = form.cleaned_data["card"]
        if card.deck_id != self.deck.id:
            return redirect("deck", slug=self.deck.slug)

        card.delete()
        return redirect("deck", slug=self.deck.slug)
