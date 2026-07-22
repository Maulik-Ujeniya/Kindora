from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.accounts.forms.login import LoginForm
from apps.accounts.forms.register import RegisterForm
from apps.accounts.models.user import User

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            return redirect("dashboard")

    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )

def logout_view(request):
    return HttpResponse("Logout Page")