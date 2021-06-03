from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'title')
    list_filter = ('is_published',)


admin.site.register(News, NewsAdmin)