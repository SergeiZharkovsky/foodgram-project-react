# Проект Foodgram

## Описание:

### Проект "**Продуктовый помощник**" это сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис "**Список покупок**" позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Как запустить проект:

#### Клонируйте репозиторий:
```
git clone
```
#### Выполните команды:
```
python -m venv env
source env/bin/activate (env/Scripts/activate)
cd backend/
python -m pip install --upgrade pip
pip install -r requirements.txt
```
#### Создайте файл .env с переменными окружения для работы с базой данных:
```
SECRET_KEY=... # укажите ваш super-key
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
#### Запустите проект:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py load_tags
python manage.py load_ingredients
python manage.py runserver
```
### Автор
Сергей Жарковский
