from django.conf.urls import url, include
from django.urls import path
from .views import (
    OrderDetailView,
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
)


urlpatterns = [
    path("order/<int:pk>", OrderDetailView.as_view(), name="order-detail"),
    path("order/<int:pk>/update", OrderUpdateView.as_view(), name="order-update"),
    path("order", OrderListView.as_view(), name="order-list"),
    path("order/add", OrderCreateView.as_view(), name="order-add"),
]
