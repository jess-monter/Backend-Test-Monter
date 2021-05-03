from django.conf.urls import url, include


urlpatterns = [
    url(r"^rest-auth/", include("rest_auth.urls")),
    url(
        r"^rest-auth/registration/",
        include("rest_auth.registration.urls"),
        name="register",
    ),
]
