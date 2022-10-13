from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-post_datetime'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

class PostDetail(DetailView):
        # Модель всё та же, но мы хотим получать информацию по отдельному товару
        model = Post
        # Используем другой шаблон — product.html
        template_name = 'newss.html'
        # Название объекта, в котором будет выбранный пользователем продукт
        context_object_name = 'newss'