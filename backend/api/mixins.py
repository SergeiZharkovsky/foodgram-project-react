from django.db.models import F

from rest_framework import mixins, viewsets
from .permissions import IsAdminOrReadOnly


class GetIsSubscribedMixin:
    """Отображение подписки на пользователя"""
    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return user.follower.filter(author=obj.id).exists()


class GetIngredientsMixin:
    """Рецепты, получение ингредиентов"""
    def get_ingredients(self, obj):
        return obj.ingredients.values(
            'id', 'name', 'measurement_unit',
            amount=F('ingredients_amount__amount')
        )


class ListRetrieveViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin):
    permission_classes = (IsAdminOrReadOnly, )
