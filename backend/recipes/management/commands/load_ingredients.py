from csv import DictReader

from django.core.management import BaseCommand
from recipes.models import Ingredient

ERROR_MESSAGE_1 = 'В базе уже есть данные!'
ERROR_MESSAGE_2 = 'Значение не определено!'
ERROR_MESSAGE_3 = 'Что-то пошло не так!'
ERROR_MESSAGE_4 = 'Все ингредиенты загружены'


class Command(BaseCommand):
    help = 'Загрузка из csv файла'

    def handle(self, *args, **kwargs):
        if Ingredient.objects.exists():
            print(ERROR_MESSAGE_1)
            return
        try:
            with open(
                './data/ingredients.csv',
                'r',
                encoding='utf-8'
            ) as file:
                reader = DictReader(file)
                Ingredient.objects.bulk_create(
                    Ingredient(**data) for data in reader)
        except ValueError:
            print(ERROR_MESSAGE_2)
        except Exception:
            print(ERROR_MESSAGE_3)
        else:
            print(ERROR_MESSAGE_4)
