from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Serializer to handle Orders."""

    class Meta:
        model = Order
        fields = "__all__"
