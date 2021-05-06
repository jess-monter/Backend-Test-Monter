from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MealViewSet, MenuViewSet

router = DefaultRouter()
router.register(r"menus", MenuViewSet, basename="menu")
router.register(r"meals", MealViewSet, basename="meal")

urlpatterns = [
    url(r"^", include(router.urls)),
]
