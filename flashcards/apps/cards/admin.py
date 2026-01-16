from django.contrib import admin
from .models import *


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'create_at',)
    list_display_links = ('name', 'content',)


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
