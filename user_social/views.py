from django.shortcuts import render, redirect
from .models import Follow_List
from django.contrib.auth.models import User
from django.contrib import messages


def follow_user(request, **kwargs):
    logged_in = User.objects.get(username=request.user.username)
    following_qs = logged_in.geek.follow.all()
    follow_to = User.objects.get(id=kwargs["pk"])

    if follow_to not in following_qs:
        logged_in.geek.follow.add(follow_to)
        messages.success(request, f"Your have started to follow {follow_to}")
    else:
        logged_in.geek.follow.remove(follow_to)
        messages.info(request, f"Your have unfollowed {follow_to}")
    return redirect("all-users")
