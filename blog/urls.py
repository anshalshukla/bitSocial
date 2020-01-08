from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("post/<int:pk>/like", views.post_like, name="post-like"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("post/new/", views.post_create, name="post-create"),
    path("post/<int:pk>/update", views.post_update, name="post-update"),
    path("post/<int:pk>/delete", views.post_delete, name="post-delete"),
    path("all_posts_user/<int:pk>", views.user_posts, name="user-posts-list"),
    path("all_users/", views.all_users, name="all-users"),
    path("pfeed/<int:pk>", views.personalised_feed, name="p-feed"),
    path("followers/", views.following_list, name="followers"),
    path("user_report", views.user_report, name="user-report"),
]
