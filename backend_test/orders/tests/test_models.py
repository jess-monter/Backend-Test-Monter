from django.test import TestCase
from django.contrib.auth.models import User
from backend_test.users.models import Employee
from backend_test.meals.models import Meal
from backend_test.orders.models import Order


class ModelTestCase(TestCase):
    """Test Orders models."""

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="john.doe", email="john.doe@cornershop.com")
        Employee.objects.create(user=user, country="CHL")

    def test_order_belongs_to_employee(self):
        """Created order belongs to employee."""

        meal = Meal.objects.create(dishes="Hot Wings with Fries and Salad")
        employee = Employee.objects.get(pk=1)
        order = Order.objects.create(meal=meal, employee=employee)
        self.assertEqual(order.employee.user.username, employee.user.username)

    def test_model_str(self):
        """Model str representation."""

        meal = Meal.objects.create(dishes="Hot Wings with Fries and Salad")
        employee = Employee.objects.get(pk=1)
        order = Order.objects.create(meal=meal, employee=employee)
        self.assertEqual(str(order), "john.doe ordered Hot Wings with Fries and Salad")
