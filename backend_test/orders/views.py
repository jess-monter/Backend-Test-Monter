from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order
from .forms import OrderForm


class OrderDetailView(LoginRequiredMixin, DetailView):
    """View for Order Details Handler."""

    model = Order

    def get_object(self, queryset=None):
        return Order.objects.get(pk=self.kwargs.get("pk"))


class OrderCreateView(LoginRequiredMixin, CreateView):
    """View for Order Creation Handler."""

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order-list")

    def form_valid(self, form):
        form.instance.employee = self.request.user.employee
        return super().form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    """View for Order List Handler."""

    model = Order

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            employee = user.employee
            queryset = Order.objects.filter(employee=employee).order_by("-created_at")
        else:
            queryset = Order.objects.all().order_by("-created_at")
        return queryset


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    """View for Order Update Handler."""

    model = Order
    fields = ["status"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("order-list")

    def get_object(self, queryset=None):
        return Order.objects.get(pk=self.kwargs.get("pk"))
