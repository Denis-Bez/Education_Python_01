from django.shortcuts import render
from django.http import HttpResponse


# request (ссылка на класс HttpRequest) содержит информацию о сессиях о куках и т.д.
def index(request):
    return HttpResponse('Страница приложения women.')

def categories(request):
    return HttpResponse('<h1>Статьи по категориям</h1>')
    