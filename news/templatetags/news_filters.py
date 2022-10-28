from django import template


register = template.Library()

# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(l):
    words_bad = ('редиска', 'сволочь', 'уроды')
    if not isinstance(l, str):
        raise TypeError('Ошибка типа')
    value = l
    for elem in value.split():
        if elem.lower() in words_bad:
            l= value.replace(elem, elem[0]+('*'*(len(elem)-1)))
            #value.replace(elem, '******')
            #f"{elem[0]}{'*'*(len(elem)-1)}")
            value = l
    return value
