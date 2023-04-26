from django import template


from ..models import MenuItem


register = template.Library()


class Tree:
    """
    Класс дерева
    """

    def __init__(self, branch, children=None):
        self.branch = branch
        self.children = children


def make_tree(ctx, parent, active_path):
    """
    Рекурсивная функция для составления дерева
    """

    children = set(filter(lambda x: x.parent == parent, ctx))
    tree = []
    if not children:
        return Tree(parent)
    for item in children:
        branch = Tree(item)
        r = make_tree(set(ctx) - children, item, active_path)
        if isinstance(r, tuple):
            branch.children = r[1]
        tree.append(branch)
    return parent, tree


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    # Для соблюдения условия, что запрос к БД должен
    # быть ровно 1, я решил получить все элементы конкретного
    # меню и из них сделал односвязный список.

    active_path = context['request'].path
    menu_items = MenuItem.objects.filter(menu__name=name)
    rez = make_tree(menu_items, None, active_path)[1]
    return {'tree': rez, 'active_path': active_path}
