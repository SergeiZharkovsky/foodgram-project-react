from django.core.management import BaseCommand
from recipes.models import Tag

ERROR_MESSAGE_1 = 'Значение не определено!'
ERROR_MESSAGE_2 = 'Что-то пошло не так!'
ERROR_MESSAGE_3 = 'Все тэги загружены.'


class Command(BaseCommand):
    help = 'Создаем тэги.'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'color': '#3DD25A', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#10B7FF', 'slug': 'lunch'},
            {'name': 'Ужин', 'color': '#F61930', 'slug': 'dinner'},
            {'name': 'Первое', 'color': '#B840CF', 'slug': 'first'},
            {'name': 'Второе', 'color': '#003153', 'slug': 'second'},
            {'name': 'Салат', 'color': '#D8FF10', 'slug': 'salad'},
        ]
        try:
            Tag.objects.bulk_create(Tag(**tag) for tag in data)
        except ValueError:
            print(ERROR_MESSAGE_1)
        except Exception:
            print(ERROR_MESSAGE_2)
        else:
            print(ERROR_MESSAGE_3)
