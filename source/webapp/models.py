from django.db import models


# Create your models here.

class Article(models.Model):
    article = models.CharField(max_length=200, verbose_name='Тема')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user = models.ForeignKey('User', max_length=40, on_delete=models.PROTECT, verbose_name='Автор', related_name='articles')

    def __str__(self):
        return self.article

class Issue(models.Model):
    STATUS_NEW = 'awful'
    STATUS_IN_PROGRESS = 'bad'
    STATUS_ON_PAUSE = 'normal'
    STATUS_DONE = 'good'
    STATUS_CANCELED = 'excellent'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Ужасно'),
        (STATUS_IN_PROGRESS, 'Плохо'),
        (STATUS_ON_PAUSE, 'Нормально'),
        (STATUS_DONE, 'Хорошо'),
        (STATUS_CANCELED, 'Отлично')
    )

    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='issues', verbose_name='Статья')
    title = models.CharField(max_length=200, verbose_name='Задача')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW, verbose_name='Статус')



class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(max_length=50, verbose_name="Почта")
    favourite = models.ManyToManyField(Article, related_name='users', verbose_name='Статьи', blank=True)

    def __str__(self):
        return "%s. %s %s" % (self.pk, self.first_name, self.last_name)


class Commentary(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='commentary')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='commentary')
    commentary = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return "%s %s" % (self.pk, self.article.article)
