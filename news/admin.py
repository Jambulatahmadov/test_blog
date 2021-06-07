from django.contrib import admin
# импорт модели
from .models import *


# новый класс который позволяет именять отоброжение моделей и новостей в админке
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_ad', 'updated_ad', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

    # list_display_links = ('id', 'title')
    # list_display = ('id', 'title')
    # list_filter = ('is_published',)


# регестрирую модель в админке
admin.site.register(News, NewsAdmin)
admin.site.register(Category)