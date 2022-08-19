from csv import DictReader

from django.core.management import BaseCommand, CommandError
# isort ругается на неожиданную пустую строку в импорте
from recipes.models import Ingredient

SOMETHING_WENT_ERROR_MESSAGE = 'Что-то пошло не так!'
INGREDIENTS_LOADED_MESSAGE = 'Все ингредиенты загружены!'


class Command(BaseCommand):
    help = 'Загрузка из csv файла'

    def handle(self, *args, **kwargs):
        try:
            with open(
                './data/ingredients.csv',
                'r',
                encoding='utf-8'
            ) as file:
                reader = DictReader(file)
                Ingredient.objects.bulk_create(
                    Ingredient(**data) for data in reader)
        except Exception:
            raise CommandError(SOMETHING_WENT_ERROR_MESSAGE)
        self.stdout.write(self.style.SUCCESS(INGREDIENTS_LOADED_MESSAGE))
