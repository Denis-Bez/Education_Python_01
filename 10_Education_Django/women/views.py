from calendar import c
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import AddPostForm
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


# request (ссылка на класс HttpRequest) содержит информацию о сессиях о куках и т.д.
def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context) # 'context' is special named parametr


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})


def addpage(request):
    
    # Don't clear fields if was error
    if request.method == 'POST':
        form = AddPostForm(request.POST) # Dictionary with filled in field
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data) # Add to database
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добваления поста')
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
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