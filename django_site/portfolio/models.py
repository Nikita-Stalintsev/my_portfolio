from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"