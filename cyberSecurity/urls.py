from django.urls import path, include
from . import views


urlpatterns = [
    path("report/<int:pk>/", views.report_offence, name="post-report"),
]
