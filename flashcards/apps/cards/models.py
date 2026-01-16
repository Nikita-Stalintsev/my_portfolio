from django.urls import reverse
from slugify import slugify
from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(verbose_name="Содержание")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deck = models.ForeignKey("Deck", on_delete=models.CASCADE, related_name="cards", null=True, verbose_name="Колода")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"


class Deck(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.CharField(max_length=255, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("deck", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Колода"
        verbose_name_plural = "Колоды"
        ordering = ('title',)
