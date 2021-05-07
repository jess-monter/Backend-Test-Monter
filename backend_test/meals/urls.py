from django.conf.urls import url, include
from django.urls import path
from .views import (
    MenuDetailView,
    MenuCreateView,
    MenuListView,
    MenuUpdateView,
    MealDetailView,
    MealCreateView,
    MealListView,
    MealUpdateView,
)

urlpatterns = [
    path("menu/<uuid:uuid>", MenuDetailView.as_view(), name="menu-detail"),
    path("menu/<uuid:uuid>/update", MenuUpdateView.as_view(), name="menu-update"),
    path("menu", MenuListView.as_view(), name="menu-list"),
    path("menu/add", MenuCreateView.as_view(), name="menu-add"),
    path("meal/<int:pk>", MealDetailView.as_view(), name="meal-detail"),
    path("meal/<int:pk>/update", MealUpdateView.as_view(), name="meal-update"),
    path("meal", MealListView.as_view(), name="meal-list"),
    path("meal/add", MealCreateView.as_view(), name="meal-add"),
]
