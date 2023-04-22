from django.shortcuts import render

from .models import MenuItem


def main(request, slug=None):
    """ Основная вьюха """

    item = MenuItem.objects.filter(slug=slug).first()
    return render(request, 'main.html', {'name': item or 'Главная страница'})
