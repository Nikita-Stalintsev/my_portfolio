from django.contrib import admin
from .models import *


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    ordering = ['id']
