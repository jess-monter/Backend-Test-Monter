from datetime import date, timedelta
from django.test import TestCase
from backend_test.meals.models import Meal, Menu


class ModelTestCase(TestCase):
    """Test Meals models."""

    def test_menu_has_a_meal(self):
        """Menu contains the number of added meals."""

        menu = Menu.objects.create(available_on=date.today())
        meal_one = Meal.objects.create(dishes="Chicken Pasta, Salad and Dessert")
        meal_two = Meal.objects.create(dishes="Plov, Salad and Dessert")
        menu.meals.set([meal_one, meal_two])
        self.assertEqual(menu.meals.count(), 2)

    def test_meal_belongs_to_menus(self):
        """Meal belongs to the number of menus to which it was added."""

        meal = Meal.objects.create(dishes="Chicken Pasta, Salad and Dessert")
        menu_one = Menu.objects.create(available_on=date.today())
        menu_two = Menu.objects.create(available_on=date.today() + timedelta(days=1))
        meal.menu_set.add(menu_one)
        meal.menu_set.add(menu_two)
        self.assertEqual(meal.menu_set.count(), 2)

    def test_model_str(self):
        """Model str representation."""

        menu = Menu.objects.create(available_on=date.today())
        meal = Meal.objects.create(dishes="Chicken Pasta, Salad and Dessert")
        self.assertEqual(str(menu), str(date.today()))
        self.assertEqual(str(meal), "Chicken Pasta, Salad and Dessert")
