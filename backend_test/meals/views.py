from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal, Menu


class MenuDetailView(DetailView):
    """View for Menu Details Handler."""

    model = Menu

    def get_object(self, queryset=None):
        menu = get_object_or_404(Menu, pk=self.kwargs.get("uuid"))
        return menu


class MenuCreateView(LoginRequiredMixin, CreateView):
    """View for Menu Creation Handler."""

    model = Menu
    fields = ["available_on", "meals"]
    success_url = reverse_lazy("menu-list")


class MenuListView(LoginRequiredMixin, ListView):
    """View for Menu List Handler."""

    model = Menu


class MenuUpdateView(LoginRequiredMixin, UpdateView):
    """View for Menu Update Handler."""

    model = Menu
    fields = ["available_on", "meals"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("menu-list")

    def get_object(self, queryset=None):
        menu = get_object_or_404(Menu, pk=self.kwargs.get("uuid"))
        return menu


class MealDetailView(LoginRequiredMixin, DetailView):
    """View for Meal Details Handler."""

    model = Meal

    def get_object(self, queryset=None):
        meal = get_object_or_404(Meal, pk=self.kwargs.get("pk"))
        return meal


class MealCreateView(LoginRequiredMixin, CreateView):
    """View for Meal Creation Handler."""

    model = Meal
    fields = ["dishes"]
    success_url = reverse_lazy("meal-list")


class MealListView(LoginRequiredMixin, ListView):
    """View for Menu List Handler."""

    model = Meal


class MealUpdateView(LoginRequiredMixin, UpdateView):
    """View for Menu Update Handler."""

    model = Meal
    fields = ["dishes"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("meal-list")

    def get_object(self, queryset=None):
        meal = get_object_or_404(Meal, pk=self.kwargs.get("pk"))
        return meal
