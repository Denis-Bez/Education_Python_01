from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# request (ссылка на класс HttpRequest) содержит информацию о сессиях о куках и т.д.
def index(request):
    return HttpResponse('Страница приложения women.')

def categories(request, catid):
    if (request.GET):
        print(request.GET) # Demonstration of extraction Get-parametrs or POST-paramentrs
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

def archive(request, year):
    if int(year) > 2020 and int(year) < 2025:
        return redirect('home') # 302-redirect
    if int(year) > 2025:
        return redirect('home', permanent=True) # 301-redirect

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')