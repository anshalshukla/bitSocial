from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.logging_in_user, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("notify/", views.notify, name="notify"),
]
