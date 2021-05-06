from datetime import date
from django.forms import ModelForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Order


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.pop("meal", None)
        super().__init__(*args, **kwargs)
        self.fields["meal"].queryset = self.fields["meal"].queryset.filter(
            menu__available_on=date.today()
        )

    def clean_meal(self):
        if timezone.now() > timezone.now().replace(hour=0, minute=30):
            raise ValidationError("The time to order is up!")

    class Meta:
        model = Order
        fields = ["meal"]
