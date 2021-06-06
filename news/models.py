from django.db import models


# создание полей модели
class News(models.Model):
    title = models.CharField('Название', max_length=150)
    content = models.TextField('Контент', blank=True)
    created_ad = models.DateTimeField('Дата публикации', auto_now_add=True)
    updated_ad = models.DateTimeField('Дата обновления', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title

    # даю имена полям чтобы корректно отоброжались в админке
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_ad']