from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    image = models.ImageField(verbose_name="Изображение", null=True)
    link = models.URLField(max_length=255, verbose_name="Ссылка")
    tags = models.ManyToManyField('ProjectTag', verbose_name="Теги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectTag(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="От кого")
    message = models.TextField(verbose_name="Содержание")
    time_send = models.DateTimeField(auto_now=True, verbose_name="Дата отправки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
