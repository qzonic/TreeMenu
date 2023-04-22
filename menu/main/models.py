from django.db import models


class Menu(models.Model):
    """ Модель меню """

    name = models.CharField(max_length=128)
    slug = models.SlugField()


class MenuItem(models.Model):
    """ Модель элементов меню """

    name = models.CharField(max_length=128)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    parent = models.ForeignKey(
        'MenuItem',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name
