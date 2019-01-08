from django.db import models


# Create your models here.

class Article(models.Model):
    article = models.CharField(max_length=200, verbose_name='Тема')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user = models.ForeignKey('User', max_length=40, on_delete=models.CASCADE, verbose_name='Автор', related_name='articles')

    def __str__(self):
        return self.article

class Issue(models.Model):
    STATUS_AWFULL = 'ужасно'
    STATUS_BAD = 'плохо'
    STATUS_NORMAL = 'нормально'
    STATUS_GOOD = 'хорошо'
    STATUS_EXCELLENT = 'отлично'

    STATUS_CHOICES = (
        (STATUS_AWFULL, 'Ужасно'),
        (STATUS_BAD, 'Плохо'),
        (STATUS_NORMAL, 'Нормально'),
        (STATUS_GOOD, 'Хорошо'),
        (STATUS_EXCELLENT, 'Отлично')
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='issues', verbose_name='Статья')
    user = models.ForeignKey('User', on_delete=models.PROTECT, related_name='issues')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_AWFULL, verbose_name='Статус')



class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(max_length=50, verbose_name="Почта")
    favourite = models.ManyToManyField(Article, related_name='users', verbose_name='Статьи', blank=True)

    def __str__(self):
        return "%s. %s %s" % (self.pk, self.first_name, self.last_name)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment')
    comment = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcomment')

    def __str__(self):
        return "%s %s" % (self.comment, self.user.first_name)
