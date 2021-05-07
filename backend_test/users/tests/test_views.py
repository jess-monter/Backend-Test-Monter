from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from backend_test.users.models import Employee


class EmployeeListViewTest(TestCase):
    """Test Employees List View."""

    @classmethod
    def setUpTestData(cls):
        """Set up initual common test data."""
        countries = ["MX", "CHL", "USA", "PER", "COL"]
        for count in range(5):
            user = User.objects.create(username=f"johny.doe {count}")
            Employee.objects.create(user=user, country=countries[count])

    def setUp(self):
        """Set up initual test data."""
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Employee view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get("/employee")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Employee list url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("employee-list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Employee list uses employee_list template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("employee-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/employee_list.html")


class EmployeeCreateViewTest(TestCase):
    """Test Employees Creation View."""

    def setUp(self):
        """Set up initual test data."""
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Employee creation view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get("/employee/add")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Employee creation url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("employee-add"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Employee creation uses employee_form template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("employee-add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/employee_form.html")


class EmployeeDetailViewTest(TestCase):
    """Test Employees Details View."""

    @classmethod
    def setUpTestData(cls):
        """Set up initual common test data."""
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()
        cls.employee = Employee.objects.create(user=mortal_user, country="CHL")

    def test_view_url_exists_at_desired_location(self):
        """Employee detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/employee/{self.employee.pk}")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Employee detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("employee-detail", kwargs={"pk": self.employee.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Employee details uses employee_detail template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("employee-detail", kwargs={"pk": self.employee.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/employee_detail.html")


class EmployeeUpdateViewTest(TestCase):
    """Test Employees Update View."""

    @classmethod
    def setUpTestData(cls):
        """Set up initual common test data."""
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()
        cls.employee = Employee.objects.create(user=mortal_user, country="CHL")

    def test_view_url_exists_at_desired_location(self):
        """Employee detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/employee/{self.employee.pk}/update")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Employee detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("employee-update", kwargs={"pk": self.employee.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Employee details uses employee_detail template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("employee-update", kwargs={"pk": self.employee.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/employee_update_form.html")
