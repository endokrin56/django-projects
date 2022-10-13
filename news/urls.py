
from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail

from . import views
from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate, PostList_, PostCreate_



urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым,

   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('articles/', PostList_.as_view(), name='articles_list'),
   path('news/', PostList.as_view(), name='post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('articles/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('articles/create/', PostCreate_.as_view(), name='articles_create'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
]

