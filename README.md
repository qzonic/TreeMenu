# Стек
<img src="https://img.shields.io/badge/Python-4169E1?style=for-the-badge"/> <img src="https://img.shields.io/badge/Django-008000?style=for-the-badge"/>

# TreeMenu
### Описание проекта:

Проект позволяет создавать древовидное меню и отрисовывать его по имени с помощью кастомного template tag.
Пункт меню, на котором пользователь находится, отображается на странице, а сам активный пункт окрашен в синий цвет.
Для отрисовки меню выполняется ТОЛЬКО один запрос к базе данных.

### Как запустить проект:

*Клонировать репозиторий и перейти в него в командной строке:*
```
https://github.com/qzonic/TreeMenu.git
```
```
cd TreeMenu/
```

*Cоздать и активировать виртуальное окружение:*
```
python -m venv venv
```
* Windows
```
venv\Scripts\activate.bat
```
* Linux/MacOS.
```
source venv/bin/activate
```

*Установить зависимости из файла requirements.txt:*
```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

*Перейдите в директорию с фалом manage.py и выполните миграции:*
```
cd menu/
```

```
python manage.py makemigrations main
```
```
python manage.py migrate
```

*Выполните загрузку тестовых данных из json в базу даных:*
```
python manage.py loaddata main.json
```

*Создать супер пользователя*
```
python manage.py createsuperuser
```

*Запустить проект:*
```
python manage.py runserver
```

### Эндпоинты для взаимодействия с проектом:

*Главная страница:*
```
/
```
*Открыть страницу конкретного пункта меню:*
```
/<str:slug>/
```

### Как устроены модели:

В проекте две модели:

* Menu - модель меню

* MenuItem - модель элементов меню

В модели "MenuItem" элемент должен ссылаться на родителя, корневые элементы ни на кого не ссылаются.
