from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from backend_test.users.models import Employee
from backend_test.meals.models import Meal
from backend_test.orders.models import Order


class OrderListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        meal_dish = "Chicken Potato"

        for count in range(5):
            User.objects.create(username=f"johny.doe {count}").save()
        users = User.objects.all()
        meals = [
            Meal.objects.create(dishes=f"{meal_dish} {count}") for count in range(5)
        ]
        employees = [
            Employee.objects.create(user=users[count], country="CHL")
            for count in range(5)
        ]

        for count in range(5):
            Order.objects.create(
                employee=employees[count],
                meal=meals[count],
                notes=f"This is a note {count}",
            )

    def setUp(self):
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Meal view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get("/order")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal list url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("order-list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal list uses meal_list template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("order-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/order_list.html")


class OrderCreateViewTest(TestCase):
    def setUp(self):
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Order creation view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get("/order/add")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Order creation url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("order-add"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Order creation uses order_form template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("order-add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/order_form.html")


class OrderDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()
        employee = Employee.objects.create(user=mortal_user, country="CHL")
        meal = Meal.objects.create(dishes="Raw Chicken and Dessert")
        cls.order = Order.objects.create(
            employee=employee, meal=meal, notes="This is a note."
        )

    def test_view_url_exists_at_desired_location(self):
        """Meal detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/order/{self.order.pk}")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("order-detail", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Order details uses order_detail template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("order-detail", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/order_detail.html")


class OrderUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()
        employee = Employee.objects.create(user=mortal_user, country="CHL")
        meal = Meal.objects.create(dishes="Raw Chicken and Dessert")
        cls.order = Order.objects.create(
            employee=employee, meal=meal, notes="This is a note."
        )

    def test_view_url_exists_at_desired_location(self):
        """Order detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/order/{self.order.pk}/update")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Order detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("order-update", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Order update uses order_update_form template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("order-update", kwargs={"pk": self.order.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/order_update_form.html")
