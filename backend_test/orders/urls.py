from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register(r"order", OrderViewSet, basename="order")

urlpatterns = [
    url(r"^", include(router.urls)),
]
