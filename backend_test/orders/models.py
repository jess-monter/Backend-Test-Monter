from django.db import models
from backend_test.users.models import Employee
from backend_test.meals.models import Meal

# Create your models here.


class Order(models.Model):

    STATUS = (("PENDING", "PENDING"), ("DELIVERED", "DELIVERED"))

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default="PENDING")
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"
