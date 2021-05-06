from rest_framework.viewsets import ModelViewSet
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal, Menu
from .serializers import MealSerializer, MenuSerializer


class MealViewSet(ModelViewSet):
    """Meal ViewSet for API ops."""

    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MenuViewSet(ModelViewSet):
    """Mene ViewSet for API ops."""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailView(DetailView):
    """View for Menu Details Handler."""

    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

    def get_object(self, queryset=None):
        return Menu.objects.get(id=self.kwargs.get("uuid"))


class MenuCreateView(LoginRequiredMixin, CreateView):
    """View for Menu Creation Handler."""

    model = Menu
    fields = ["available_on", "meals"]
    success_url = reverse_lazy("menu-list")


class MenuListView(LoginRequiredMixin, ListView):
    """View for Menu List Handler."""

    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class MenuUpdateView(LoginRequiredMixin, UpdateView):
    """View for Menu Update Handler."""

    model = Menu
    fields = ["available_on", "meals"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("menu-list")

    def get_object(self, queryset=None):
        return Menu.objects.get(id=self.kwargs.get("uuid"))


class MealDetailView(LoginRequiredMixin, DetailView):
    """View for Meal Details Handler."""

    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

    def get_object(self, queryset=None):
        return Meal.objects.get(pk=self.kwargs.get("pk"))


class MealCreateView(LoginRequiredMixin, CreateView):
    """View for Meal Creation Handler."""

    model = Meal
    fields = ["dishes"]
    success_url = reverse_lazy("meal-list")


class MealListView(LoginRequiredMixin, ListView):
    """View for Menu List Handler."""

    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class MealUpdateView(LoginRequiredMixin, UpdateView):
    """View for Menu Update Handler."""

    model = Meal
    fields = ["dishes"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("meal-list")

    def get_object(self, queryset=None):
        return Meal.objects.get(pk=self.kwargs.get("pk"))
