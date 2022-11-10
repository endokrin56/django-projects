# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from .models import Post
#
# # Create your views here.
# class PostList(ListView):
#     # Указываем модель, объекты которой мы будем выводить
#     model = Post
#     # Поле, которое будет использоваться для сортировки объектов
#     ordering = '-post_datetime'
#     # Указываем имя шаблона, в котором будут все инструкции о том,
#     # как именно пользователю должны быть показаны наши объекты
#     template_name = 'news.html'
#     # Это имя списка, в котором будут лежать все объекты.
#     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'news'
#
# class PostDetail(DetailView):
#         # Модель всё та же, но мы хотим получать информацию по отдельному товару
#         model = Post
#         # Используем другой шаблон — product.html
#         template_name = 'newss.html'
#         # Название объекта, в котором будет выбранный пользователем продукт
#         context_object_name = 'newss'
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView
# from .models import Post

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, Textarea
from django.shortcuts import render
from django.template.defaultfilters import pprint
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Category
from .filters import PostFilter
from django.urls import reverse_lazy
from django_filters import ModelChoiceFilter, DateTimeFilter
from django.forms import DateInput
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView
from .models import Post
from .tasks import  send_mail_c, hello

        # Create your views here.

        # def seach(request):
        #     return HttpResponse('<h1>seach</h1>')

@login_required
def show_protected_page(request):
            # // do something protected
            pass

class PostForm(ModelForm):
            class Meta:
                model = Post
                category = ModelChoiceFilter(
                    lookup_expr='exact',
                    queryset=Category.objects.all(),
                    label='Категория',
                    field_name='category',
                )

                fields = ['author', 'category', 'headPost', 'textPost', 'typePost']

                widgets = {
                    'textPost': Textarea(attrs={'cols': 25, 'rows': 5}),
                }

class PostSearch(ListView):
            model = Post
            template_name = 'search.html'
            context_object_name = 'search'
            paginate_by = 10

            # Переопределяем функцию получения списка товаров
            def get_queryset(self):
                # Получаем обычный запрос
                queryset = super().get_queryset()
                # Используем наш класс фильтрации.
                # self.request.GET содержит объект QueryDict, который мы рассматривали
                # в этом юните ранее.
                # Сохраняем нашу фильтрацию в объекте класса,
                # чтобы потом добавить в контекст и использовать в шаблоне.
                self.filterset = PostFilter(self.request.GET, queryset)
                # Возвращаем из функции отфильтрованный список новостей
                return self.filterset.qs

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                # Добавляем в контекст объект фильтрации.
                context['filterset'] = self.filterset
                return context

# class PostList(ListView):
#             Указываем модель, объекты которой мы будем выводить
            # model = Post


# class PostList(ListView):
#             # Это имя списка, в котором будут лежать все объекты.
#             # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#             context_object_name = 'news'
#             paginate_by = 10

class PostDetail(DetailView):
            # Модель всё та же, но мы хотим получать информацию по отдельному
            model = Post
            # Используем другой шаблон — product.html
            template_name = 'newss.html'
            # Название объекта, в котором будет выбранный пользователем
            context_object_name = 'newss'

            # paginate_by = 10  # вот так мы можем указать количество записей на странице

            # Переопределяем функцию получения списка новостей
            def get_queryset(self):
                # pprint(self.context_object_name.title())
                # Получаем обычный запрос
                # queryset = super().get_queryset()
                queryset = Post.objects.filter(typePost='NW')
                # Используем наш класс фильтрации.
                # self.request.GET содержит объект QueryDict, который мы рассматривали
                # в этом юните ранее.
                # Сохраняем нашу фильтрацию в объекте класса,
                # чтобы потом добавить в контекст и использовать в шаблоне.
                self.filterset = PostFilter(self.request.GET, queryset)
                # Возвращаем из функции отфильтрованный список товаров
                return self.filterset.qs

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                # Добавляем в контекст объект фильтрации.
                context['filterset'] = self.filterset
                return context


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
    paginate_by = 10  # вот так мы можем указать количество записей на странице
    # hello.delay()
    # Переопределяем функцию получения списка новостей
    def get_queryset(self):
        # pprint(self.context_object_name.title())
        # Получаем обычный запрос
        # queryset = super().get_queryset()
        queryset = Post.objects.filter(typePost='NW')
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset

        return context

class PostList_(ListView):
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
            paginate_by = 10  # вот так мы можем указать количество записей на странице
            # hello.delay()
            # Переопределяем функцию получения списка новостей
            def get_queryset(self):
                # pprint(self.context_object_name.title())
                # Получаем обычный запрос
                # queryset = super().get_queryset()
                queryset = Post.objects.filter(typePost='AR')
                # Используем наш класс фильтрации.
                # self.request.GET содержит объект QueryDict, который мы рассматривали
                # в этом юните ранее.
                # Сохраняем нашу фильтрацию в объекте класса,
                # чтобы потом добавить в контекст и использовать в шаблоне.
                self.filterset = PostFilter(self.request.GET, queryset)
                # Возвращаем из функции отфильтрованный список товаров
                return self.filterset.qs

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                # Добавляем в контекст объект фильтрации.
                context['filterset'] = self.filterset
                return context

class PostDetail(DetailView):
            # Модель всё та же, но мы хотим получать информацию по отдельной новости
            model = Post
            # Используем другой шаблон
            template_name = 'newss.html'
            # Название объекта, в котором будет выбранная пользователем новость
            context_object_name = 'newss'

        # class PostCreate(LoginRequiredMixin, CreateView):
class PostCreate(PermissionRequiredMixin, CreateView):
            permission_required = ('news.add_post',)
            # определяем форму
            form_class = PostForm
            #  отвечает за перепосыл при ограничении доступа
            raise_exception = True
            # Модель всё та же, но мы хотим получать информацию по отдельной новости
            model = Post
            # определяем поля
            # fields = '__all__'
            # Используем другой шаблон
            template_name = 'newss_create.html'
            # Название объекта, в котором будет выбранный пользователем новость
            context_object_name = 'create'
            success_url = reverse_lazy('post_list')
            # hello.delay()
            send_mail_c.delay()

            def form_valid(self, form):
                post = form.save(commit=False)
                post.typePost = 'NW'
                # hello.delay()
                send_mail_c.delay()
                return super().form_valid(form)

            # def get_absolute_url(self):
            #  self   return f'/news/{self.name}/'

        # class PostCreate_(LoginRequiredMixin, CreateView):
class PostCreate_(PermissionRequiredMixin, CreateView):
            permission_required = ('news.add_post',)
            # определяем форму
            form_class = PostForm
            #  отвечает за перепосыл при ограничении доступа
            raise_exception = True
            # Модель всё та же, но мы хотим получать информацию по отдельной новости
            model = Post
            # определяем поля
            # fields = '__all__'
            # Используем другой шаблон
            template_name = 'newss_create.html'
            # Название объекта, в котором будет выбранный пользователем новость
            context_object_name = 'create'
            success_url = reverse_lazy('articles_list')
            #hello.delay()
         
            def form_valid(self, form):
                post = form.save(commit=False)
                post.typePost = 'AR'
                #hello.delay()
                send_mail_c.delay()
                return super().form_valid(form)

        # Представление удаляемой новость.
class PostDelete(PermissionRequiredMixin, DeleteView):
            permission_required = ('news.delete_post',)
            model = Post
            template_name = 'newss_delete.html'
            success_url = reverse_lazy('post_list')

class PostUpdate(PermissionRequiredMixin, UpdateView):
            permission_required = ('news.change_post',)
            form_class = PostForm
            model = Post
            template_name = 'newss_create.html'
            success_url = reverse_lazy('post_list')

            # Название объекта, в котором будет выбранный пользователем продукт
            context_object_name = 'newss'

class CategoryList(ListView):
    model = Post
    # определяем поля
    fields = '__all__'
    # Используем  шаблон
    template_name = 'category_list.html'
    context_object_name = 'categorynews'

    # Переопределяем функцию получения списка новостей
    def get_queryset(self):
        # Получаем обычный запрос
        #queryset = super().get_queryset()
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-post_datetime')
        return  queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['is_not_mailing'] = self.request.user not in self.category.mailing.all()
        context['category'] = self.category
        return context


@login_required
def mailings(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.mailing.add(user)
    #hello.delay()
    message =' Вы подписались на рассылку '

    return render(request, 'mailing.html', {'category':category, 'message':message})

