from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *
menu = ['About', 'Add article', 'Feedback', 'Sing in']

# request (ссылка на класс HttpRequest) содержит информацию о сессиях о куках и т.д.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main Page'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})

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