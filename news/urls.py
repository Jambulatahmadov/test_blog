from django.urls import path
# импорт всех функций из вьюхи
from .views import *
# указываю маршрут url, при каком адресе подключать ту или иную функцию
urlpatterns = [
    path('', index),
    path('about/', about),
]