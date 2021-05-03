from django.db import models

# Create your models here.


class Meal(models.Model):

    dishes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "meal"
        verbose_name = "Meal"
        verbose_name_plural = "Meals"

    def __str__(self):
        return self.dishes


class Menu(models.Model):
    meals = models.ManyToManyField(Meal, through="MenuMeal")
    available_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "menu"
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


class MenuMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "menu_meals"
        verbose_name = "Menu Meal"
        verbose_name_plural = "Menus Meals"
        unique_together = ("meal", "menu")
