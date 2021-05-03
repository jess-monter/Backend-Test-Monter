from rest_framework import serializers
from .models import Menu, Meal


class MealSerializer(serializers.ModelSerializer):
    """Serializer to handle Dishes. """

    class Meta:
        model = Meal
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    """Serializer to handle Menus. """

    meals = MealSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ("available_on", "meals")
