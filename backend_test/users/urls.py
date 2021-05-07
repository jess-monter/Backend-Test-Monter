from django.conf.urls import url, include
from django.urls import path
from .views import (
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeListView,
    EmployeeUpdateView,
)


urlpatterns = [
    url(r"^rest-auth/", include("rest_auth.urls")),
    url(
        r"^rest-auth/registration/",
        include("rest_auth.registration.urls"),
        name="register",
    ),
    path("accounts/", include("allauth.urls")),
    path("employee/<int:pk>", EmployeeDetailView.as_view(), name="employee-detail"),
    path(
        "employee/<int:pk>/update", EmployeeUpdateView.as_view(), name="employee-update"
    ),
    path("employee", EmployeeListView.as_view(), name="employee-list"),
    path("employee/add", EmployeeCreateView.as_view(), name="employee-add"),
]
