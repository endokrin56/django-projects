from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        lookup_expr='exact',
        queryset=Category.objects.all(),
        label='Категория',
    )
    post_datetime = DateTimeFilter(field_name='post_datetime',
                             lookup_expr='lt',
                             label='Дата публикации',
                             widget= DateInput(
                             format='%d-%m-%Y',
                             attrs={'type': 'datetime-local'})
                             )
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        # по       названию;
        # по       категории;
        # позже       указываемой       даты
        fields = {
            # поиск по названию
            'headPost': ['icontains'],
            # количество товаров должно быть больше или равно
            'category': ['exact'],
            #'post_datetime': ['gt'],
            #    'range',  # дата должна быть меньше
            #    #'gte',  # дата должна быть больше
            # ],
        }
