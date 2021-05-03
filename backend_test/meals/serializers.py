from rest_framework import serializers
from .models import Menu, Meal


class MealSerializer(serializers.ModelSerializer):
    """Serializer to handle Dishes. """

    class Meta:
        model = Meal
        exclude = ("created_at", "updated_at")


class MenuSerializer(serializers.ModelSerializer):
    """Serializer to handle Menus. """

    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        exclude = ("created_at", "updated_at")
