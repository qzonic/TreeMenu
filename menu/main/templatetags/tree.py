from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from ..models import MenuItem

register = template.Library()


def make_tree(ctx, parent, active_path):
    # Тут скорее всего можно воспользоваться шаблонизатором,
    # но, к сожалению, мне не хватило времени допилить его,
    # поэтому принял решенил построить html прям в коде

    tr = set(filter(lambda x: x.parent == parent, ctx))
    if not tr:
        return '<li>' + parent.name + '</li>'
    tree = ''
    for i, item in enumerate(tr, start=1):
        if i == 1:
            tree += f'<ul class="{"submenu" if item.parent else "topmenu"}">'
        tree += '<li>'
        url = reverse('main-slug', kwargs={'slug': item.slug})
        tree += f'<a href="{url}" class="{"active" if item.slug in active_path else ""}">{item.name}</a>'
        r = make_tree(set(ctx)-tr, item, active_path)
        if isinstance(r, tuple):
            tree += r[1]
        tree += '</li>'
        if i == len(tr):
            tree += '</ul>'
    return parent, tree


@register.inclusion_tag('method_second.html', takes_context=True)
def draw_menu(context, name, parent_id=None):

    # Способ 1. Правильнее было бы сделать вот таким способом,
    # но так как есть условие, что запрос к БД должн быть ровно 1
    # такое решение не подходи, потому что при рекурсии в шаблоне
    # количество запросов к БД будет равно количеству элементов в меню.
    # Использовать шаблан method_first.html

    # if parent_id:
    #     menu_items = MenuItem.objects.select_related().filter(
    #         menu__name=name,
    #         parent__id=parent_id
    #     )
    # else:
    #     menu_items = MenuItem.objects.select_related().filter(
    #         menu__name=name,
    #         parent=parent_id
    #     )
    # return {'menu_items': menu_items, 'request': context['request'], 'children': bool(menu_items)}

    # Способ 2. Для соблюдения условия, что запрос к БД должен
    # быть ровно 1, я решил получить все элементы конкретного
    # меню и средствами python построить из них дерего этого меню
    # с помощью функции make_tree. В результате этого способа
    # получается html код и всавляется в шаблон.
    # Использовать шаблан method_second.html

    active_path = context['request'].path
    menu_items = MenuItem.objects.filter(menu__name=name)
    rez = make_tree(menu_items, None, active_path)[1]
    return {"result": mark_safe(rez)}
