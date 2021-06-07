from django.shortcuts import render
# импортирую модель чтобы работать с нею в функциях вьюхи
from .models import *


# рендер шаблона с передачей в него новостей из модели
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }
    return render(request, 'news/index.html', context)


def about(request):
    return render(request, 'news/about.html')

