from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MenuViewSet, menu_detail

router = DefaultRouter()
router.register(r"menu", MenuViewSet, basename="menu"),

urlpatterns = [
    url(r"^", include(router.urls)),
    path("menu/<int:menu_id>", menu_detail, name="menu-detail"),
]
