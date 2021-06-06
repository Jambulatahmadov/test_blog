from django.contrib import admin
# импорт модели
from .models import News


# новый класс который позволяет именять отоброжение моделей и новостей в вдминке
class NewsAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'title')
    list_filter = ('is_published',)


# регестрирую модель в админке
admin.site.register(News, NewsAdmin)