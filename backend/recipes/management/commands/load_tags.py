from django.core.management import BaseCommand, CommandError

from recipes.models import Tag

SOMETHING_WENT_ERROR_MESSAGE = 'Что-то пошло не так!'
TAGS_LOADED_MESSAGE = 'Все тэги загружены!'


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
        except Exception:
            raise CommandError(SOMETHING_WENT_ERROR_MESSAGE)
        else:
            print(TAGS_LOADED_MESSAGE)
