# Проект Foodgram

![Foodgram project workflow Status](https://github.com/SergeiZharkovsky/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?branch=main&event=push)

Адрес сайта: http://84.252.141.85/recipes/

Админка: http://84.252.141.85/admin/ (login: Sergei pass: Sergei123456789)

## Описание:

### Проект "**Продуктовый помощник**" это сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис "**Список покупок**" позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Технологии
- Python
- Django
- Django Rest Framework
- Docker
- Gunicorn
- NGINX
- PostgreSQL

## Как запустить проект:

#### Клонируйте репозиторий:
```
git clone git@github.com:SergeiZharkovsky/foodgram-project-react.git
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
#### Сборка и запуск:
```
cd foodgram-project-react/infra/
docker-compose up -d --build
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py load_tags
docker-compose exec backend python manage.py load_ingredients
```
### Автор
Сергей Жарковский
