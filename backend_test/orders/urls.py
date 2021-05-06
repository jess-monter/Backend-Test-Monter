from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    OrderViewSet,
    OrderDetailView,
    OrderListView,
    OrderCreateView,
    OrderUpdateView,
)

router = DefaultRouter()
router.register(r"order", OrderViewSet, basename="order")

urlpatterns = [
    url(r"^", include(router.urls)),
    path("order/<int:pk>", OrderDetailView.as_view(), name="order-detail"),
    path("order/<int:pk>/update", OrderUpdateView.as_view(), name="order-update"),
    path("order", OrderListView.as_view(), name="order-list"),
    path("order/add", OrderCreateView.as_view(), name="order-add"),
]
