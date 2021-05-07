from datetime import date, timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from backend_test.meals.models import Meal, Menu


class MealListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        meals_count = 13
        meal_dish = "Chicken Potato"

        for count in range(meals_count):
            Meal.objects.create(dishes=f"{meal_dish} {count}")

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
        response = self.client.get("/meal")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal list url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal list uses meal_list template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/meal_list.html")


class MealCreateViewTest(TestCase):
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
        """Meal creation view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get("/meal/add")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal creation url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-add"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal creation uses meal_form template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/meal_form.html")


class MealDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.meal = Meal.objects.create(dishes="Raw Chicken and Dessert")
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Meal detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/meal/{self.meal.pk}")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-detail", kwargs={"pk": self.meal.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal details uses meal_detail template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-detail", kwargs={"pk": self.meal.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/meal_detail.html")


class MealUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.meal = Meal.objects.create(dishes="Raw Chicken and Dessert")
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Meal detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/meal/{self.meal.pk}/update")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-update", kwargs={"pk": self.meal.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal details uses meal_detail template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("meal-update", kwargs={"pk": self.meal.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/meal_update_form.html")


class MenuListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        menus_count = 13

        for count in range(menus_count):
            Menu.objects.create(available_on=date.today() + timedelta(days=count))

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
        response = self.client.get("/menu")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal list url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("menu-list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal list uses meal_list template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("menu-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/menu_list.html")


class MenuCreateViewTest(TestCase):
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
        response = self.client.get("/menu/add")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Meal creation url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("menu-add"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Meal creation uses meal_form template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(reverse("menu-add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/menu_form.html")


class MenuDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(available_on=date.today())
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Menu detail view exists at url."""
        response = self.client.get(f"/menu/{self.menu.pk}")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Menu detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("menu-detail", kwargs={"uuid": self.menu.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Menu details uses menu_detail template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("menu-detail", kwargs={"uuid": self.menu.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/menu_detail.html")


class MenuUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(available_on=date.today())
        super_user = User.objects.create_user(
            username="john.doe", password="XVAP11!0$", is_superuser=True
        )
        super_user.save()
        mortal_user = User.objects.create_user(
            username="jane.doe", password="XVAP12!0$"
        )
        mortal_user.save()

    def test_view_url_exists_at_desired_location(self):
        """Menu detail view exists at url."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(f"/menu/{self.menu.pk}/update")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        """Menu detail url is accesible by its name."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("menu-update", kwargs={"uuid": self.menu.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Menu update uses menu_update_form template."""
        self.client.login(username="john.doe", password="XVAP11!0$")
        response = self.client.get(
            reverse("menu-update", kwargs={"uuid": self.menu.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals/menu_update_form.html")
