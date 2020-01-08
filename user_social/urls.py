from django.urls import path, include
from . import views


urlpatterns = [
    path("follow/<int:pk>", views.follow_user, name="follow-user"),
]
