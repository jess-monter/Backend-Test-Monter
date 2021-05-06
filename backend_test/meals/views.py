from rest_framework.viewsets import ModelViewSet
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Meal, Menu
from .serializers import MealSerializer, MenuSerializer

# Create your views here.


class MealViewSet(ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MenuViewSet(ModelViewSet):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetailView(DetailView):

    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

    def get_object(self, queryset=None):
        return Menu.objects.get(id=self.kwargs.get("uuid"))


class MenuCreateView(CreateView):

    model = Menu
    fields = ["available_on", "meals"]
    success_url = reverse_lazy("menu-list")


class MenuListView(ListView):

    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class MenuUpdateView(UpdateView):
    model = Menu
    fields = ["available_on", "meals"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("menu-list")

    def get_object(self, queryset=None):
        return Menu.objects.get(id=self.kwargs.get("uuid"))


class MealDetailView(DetailView):

    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

    def get_object(self, queryset=None):
        return Meal.objects.get(pk=self.kwargs.get("pk"))


class MealCreateView(CreateView):

    model = Meal
    fields = ["dishes"]
    success_url = reverse_lazy("meal-list")


class MealListView(ListView):

    model = Meal

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class MealUpdateView(UpdateView):
    model = Meal
    fields = ["dishes"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("meal-list")

    def get_object(self, queryset=None):
        return Meal.objects.get(pk=self.kwargs.get("pk"))
