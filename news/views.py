from django.shortcuts import render
# импортирую модель чтобы работать с нею в функциях вьюхи
from .models import News


# рендер шаблона с передачей в него новостей из модели
def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})


def about(request):
    return render(request, 'news/about.html')

