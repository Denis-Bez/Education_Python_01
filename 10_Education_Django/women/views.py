from calendar import c
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Class-Based Views
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import AddPostForm
from .models import *
from .utils import *


class WomenHome(DataMixin, ListView):
    # paginate_by = 3 # Class "Paginator" embedded in "ListView". Relocate to mixin
    model = Women
    template_name = 'women/index.html' # Django search (by default) template in path - "<app name>/<model name>_list.html"
    context_object_name = 'posts' # By default 'object_list'
    # extra_context = {'title': 'Главная страница'} # Only static data

    # Transfer dynamic data to template
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # The context that has already been formed
        c_def = self.get_user_context_data(title='Главная страница') # metod from mixin
        return dict(list(context.items()) + list(c_def.items()))
    
    # Filter for data 'Women' than must be readed
    def get_queryset(self):
        return Women.objects.filter(is_published=True)
    


# request (ссылка на класс HttpRequest) содержит информацию о сессиях о куках и т.д.
# def index(request):
#     posts = Women.objects.all()

#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context) # 'context' is special named parametr


# @login_required # Access only authorized users (decorators for function, mixins for classes)
def about(request):
    # Pagination in view fuction
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'About site'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home') # default url from 'models.get_absolute_url'
    login_url = reverse_lazy('home') # If user unauthorized or `raiser_exception = True`

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # The context that has already been formed
        c_def = self.get_user_context_data(title = 'Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     # Don't clear fields if was error
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES) # Dictionary with filled in field
       
#         # Checking and Add to database, for Option 1 in 'forms.py'
#         # if form.is_valid():
#         #     print(form.cleaned_data)
#         #     try:
#         #         Women.objects.create(**form.cleaned_data) 
#         #         return redirect('home')
#         #     except:
#         #         form.add_error(None, 'Ошибка добваления поста')
        
#         if form.is_valid():
#             form.save() # Save to database
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)

#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'women/post.html', context=context)


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'post_pk' # If We don't use slug
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context_data(title = context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # If there are no records, rendering page '404 error'

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], 
            is_published=True)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context_data(title ='Категория - ' + str(context['posts'][0].cat),
                                           cat_selected=context['posts'][0].cat)
        return dict(list(context.items()) + list(c_def.items()))
        

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'View Categories',
#         'cat_selected': cat_id,
#     }

#     return render(request, 'women/index.html', context=context)


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