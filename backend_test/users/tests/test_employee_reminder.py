from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from backend_test.users.models import Employee
from backend_test.meals.models import Menu, Meal
from backend_test.users.employee_reminder import EmployeeReminder


class EmployeeReminderTest(TestCase):
    """Test slack notifications handler."""

    @classmethod
    def setUpTestData(cls):
        """Set up initual common test data."""
        countries = ["MX", "CHL", "USA", "PER", "COL"]
        slack_user_ids = ["UP0918MAV", "UP0918MAV", "UP0918MAV", None, None]
        cls.menu = Menu.objects.create(available_on=date.today())
        for count in range(5):
            user = User.objects.create(username=f"johny.doe {count}")
            Employee.objects.create(
                user=user, country=countries[count], slack_user_id=slack_user_ids[count]
            )

    def test_get_menu_url(self):
        site = Site.objects.get_current()
        site.domain = "https://test-domain/"
        site.save()
        menu_url = EmployeeReminder("CHL").get_menu_url()
        test_menu_url = site.domain + str(self.menu.id)
        self.assertEqual(menu_url, test_menu_url)

    def test_get_new_menu(self):
        menu_pk = EmployeeReminder("CHL").get_new_menu()
        self.assertEqual(menu_pk, str(self.menu.id))

    def test_get_employees_slack_ids(self):
        employees = EmployeeReminder("CHL").get_employees_slack_ids()
        self.assertEqual(employees, ["UP0918MAV"])
