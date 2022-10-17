from calendar import c
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

# request (ссылка на класс HttpRequest) содержит информацию о сессиях о куках и т.д.
def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context) # 'context' is special named parametr

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'View Categories',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)

# def categories(request, catid):
#     if (request.GET):
#         print(request.GET) # Demonstration of extraction Get-parametrs or POST-paramentrs
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')

# def archive(request, year):
#     if int(year) > 2020 and int(year) < 2025:
#         return redirect('home') # 302-redirect
#     if int(year) > 2025:
#         return redirect('home', permanent=True) # 301-redirect
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')