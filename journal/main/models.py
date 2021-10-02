from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class News(models.Model):
    name = models.CharField('Название поста', max_length=160)
    post = models.TextField('Текст поста')
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    date = models.DateTimeField('Дата добавления', default=timezone.now())

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
