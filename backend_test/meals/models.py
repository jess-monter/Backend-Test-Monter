from django.db import models

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "dish"
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"


class Menu(models.Model):
    dishes = models.ManyToManyField(Dish, through="MenuDish")
    available_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "menu"
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


class MenuDish(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "menu_dishes"
        verbose_name = "Menu Dish"
        verbose_name_plural = "Menus Dishes"
