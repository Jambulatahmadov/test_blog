from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    content = models.TextField('Контент', blank=True)
    created_ad = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)