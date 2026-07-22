from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.accounts.forms.login import LoginForm
from apps.accounts.forms.register import RegisterForm

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
    form = RegisterForm()
    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )

def logout_view(request):
    return HttpResponse("Logout Page")