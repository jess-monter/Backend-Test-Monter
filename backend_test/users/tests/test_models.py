from django.test import TestCase
from django.contrib.auth.models import User
from backend_test.users.models import Employee


class ModelTestCase(TestCase):
    """Test Users models."""

    def test_user_belongs_to_employee(self):
        """User is related to Employee."""
        user = User.objects.create(username="john.doe", email="john.doe@cornershop.com")
        employee = Employee.objects.create(user=user, country="CHL")
        self.assertEqual(employee.user.pk, user.pk)

    def test_employee_belongs_to_user(self):
        """Employee is related to user."""
        user = User.objects.create(
            username="johny.doe", email="johny.doe@cornershop.com"
        )
        employee = Employee.objects.create(user=user, country="CHL")
        self.assertEqual(user.employee.pk, employee.pk)

    def test_model_str(self):
        """Model str representation."""
        user = User.objects.create(username="jane.doe", email="jane.doe@cornershop.com")
        employee = Employee.objects.create(user=user, country="CHL")
        self.assertEqual(str(employee), "jane.doe")
