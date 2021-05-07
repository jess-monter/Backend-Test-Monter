from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """View for Employee Details Handler."""

    model = Employee

    def get_object(self, queryset=None):
        employee = get_object_or_404(Employee, pk=self.kwargs.get("pk"))
        return employee


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    """View for Employee Creation Handler."""

    model = Employee
    fields = ["user", "country", "slack_user_id"]
    success_url = reverse_lazy("employee-list")


class EmployeeListView(LoginRequiredMixin, ListView):
    """View for Menu List Handler."""

    model = Employee


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    """View for Menu Update Handler."""

    model = Employee
    fields = ["user", "country", "slack_user_id"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("employee-list")

    def get_object(self, queryset=None):
        employee = get_object_or_404(Employee, pk=self.kwargs.get("pk"))
        return employee
