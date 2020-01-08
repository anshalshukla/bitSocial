from django.shortcuts import render, redirect
from .forms import (
    UserRegisterForm,
    UserVerificationForm,
    UserUpdateForm,
    ProfileUpdateForm,
)
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account Created for {username}!")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def logging_in_user(request):
    if request.method == "POST":
        form = UserVerificationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("blog-home")
        else:
            print(messages.warning(request, f"Check your Credentials!"))
            return redirect("login")
    else:
        form = UserVerificationForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def logout_view(request):
    messages.success(
        request, f"{request.user.username} has been successfully logged out."
    )
    logout(request)
    return render(request, "users/logout.html")


@login_required
def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        try:
            if u_form.is_valid and p_form.is_valid:
                u_form.save()
                p_form.save()
                messages.success(
                    request, f"Your account has been successfully Updated!"
                )
                return redirect("profile")
        except Exception as e:
            messages.warning(request, f"{e}")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)


@login_required
def notify(request):
    if request.user.profile.notify:
        request.user.profile.notify = False
        request.user.profile.save()
    else:
        request.user.profile.notify = True
        request.user.profile.save()

    return redirect("profile")
